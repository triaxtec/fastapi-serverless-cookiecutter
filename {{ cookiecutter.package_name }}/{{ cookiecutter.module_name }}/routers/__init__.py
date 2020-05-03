from fastapi import FastAPI


def register_routers(app: FastAPI):
    """ Register routers against the app """
    from . import default

    default.register_router(app)
