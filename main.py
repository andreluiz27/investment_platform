from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import account_router, auth_router, position_router


app = FastAPI()
app.include_router(account_router)
app.include_router(auth_router)
app.include_router(position_router)

from fastapi_simple_cache import FastAPISimpleCache

from fastapi_simple_cache.backends.inmemory import InMemoryBackend

# Initialize in startup event


def init_db():
    from models.account import Account  # noqa

    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    backend = InMemoryBackend()
    FastAPISimpleCache.init(backend)

    # Create all tables
    init_db()
