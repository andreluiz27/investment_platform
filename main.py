from fastapi import FastAPI
from database import engine, Base
from routers import account_router, auth_router, position_router


app = FastAPI(
    Title="Investor's API",
    Description="API for investors to manage their accounts and positions",
)
app.include_router(account_router)
app.include_router(auth_router)
app.include_router(position_router)

from fastapi_simple_cache import FastAPISimpleCache  # noqa

from fastapi_simple_cache.backends.inmemory import InMemoryBackend  # noqa

# Initialize in startup event


def init_db():
    from models.account import Account  # noqa
    from models.position import Position  # noqa

    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    backend = InMemoryBackend()
    FastAPISimpleCache.init(backend)

    # Create all tables
    init_db()
