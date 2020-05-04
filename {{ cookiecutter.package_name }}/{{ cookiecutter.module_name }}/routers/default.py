from functools import lru_cache
from pathlib import Path

from fastapi import APIRouter, Depends, FastAPI
from markdown import markdown
from starlette.responses import HTMLResponse

router = APIRouter()


def register_router(app: FastAPI) -> None:
    """ Register this router against the application """
    app.include_router(router)


@lru_cache
def _get_changelog_html() -> bytes:
    changelog_path: Path = Path(__file__).parent.parent / "CHANGELOG.md"
    _changelog_html = markdown(changelog_path.read_text())
    return _changelog_html


@router.get("/changelog", response_class=HTMLResponse)
async def changelog() -> HTMLResponse:
    """ Display the changelog for this API """
    return HTMLResponse(content=_get_changelog_html())
