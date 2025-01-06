from fastapi import FastAPI

from .container import Container
from .endpoints import router


def create_app() -> FastAPI:
    app_ = FastAPI()
    app_.container = Container() # type: ignore
    app_.include_router(router)
    return app_


app = create_app()