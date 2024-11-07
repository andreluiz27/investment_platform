import asyncio
import datetime
import httpx

from fastapi import APIRouter
from database import get_db
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from schemas import Token, TokenData
from dependencies import authenticate_user, create_access_token
from datetime import timedelta
from fastapi import HTTPException, status
from constants import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(prefix="/auth")


@router.post("/token")
async def login_for_access_token(
    form: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)
) -> Token:

    account = await authenticate_user(form.username, form.password, db)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": account.cpf}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
