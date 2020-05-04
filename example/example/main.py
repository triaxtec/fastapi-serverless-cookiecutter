import re
from importlib.metadata import version
from typing import Awaitable, Callable

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.routing import APIRoute
from secure import SecureHeaders
from semantic_version import Version
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from . import database
from .config import get_config
from .routers import register_routers

# Convert PyPIs non-standard versioning to real semver
app_version = str(Version.coerce(version(__package__)))
if (match := re.match(r".+\-(\D+)(\d+)", app_version)) is not None:  # pragma: nocover
    # Pre-release, gotta set the version correctly
    pre_release_str = match.group(1)
    pre_release_num = match.group(2)
    app_version = app_version.replace(f"{pre_release_str}{pre_release_num}", f"{pre_release_str}.{pre_release_num}")

app = FastAPI(title="example", description="A very Fast API", version=app_version)
database.init_db()
register_routers(app)

# Clean up operation IDs for better generated function names
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name

_config = get_config()

if sentry_url := _config.get("sentry/url"):  # pragma: no cover
    import sentry_sdk
    from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
    from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
    from sentry_sdk.integrations.aiohttp import AioHttpIntegration

    sentry_sdk.init(
        sentry_url,
        environment=_config["env"],
        integrations=[SqlalchemyIntegration(), AioHttpIntegration()],
        release=f"example@{app_version}",
    )
    app.add_middleware(SentryAsgiMiddleware)


if scout_config := _config.get("scout"):  # pragma: no cover
    from scout_apm.api import Config
    from scout_apm.async_.starlette import ScoutMiddleware

    Config.set(
        key=scout_config["key"],
        name=f"example {_config['env'].capitalize()}",
        monitor=True,
        revision_sha=app_version,
    )
    app.add_middleware(ScoutMiddleware)

_secure_headers = SecureHeaders()
app.add_middleware(
    CORSMiddleware, allow_origins="*", allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
app.add_middleware(GZipMiddleware)


@app.middleware("http")
async def _set_secure_headers(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    response = await call_next(request)
    _secure_headers.starlette(response)
    return response
