import jwt

from typing import Union, Annotated
from constants import SECRET_KEY, ALGORITHM
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone

from schemas.auth import TokenData
from utils.auth import verify_password
from crud.account import get_account_by_cpf
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def authenticate_user(cpf: str, password: str, db):
    account = await get_account_by_cpf(db, cpf)
    if not account:
        return False
    if not verify_password(password, account.hashed_password):
        return False
    return account


async def get_current_account(
    token: Annotated[str, Depends(oauth2_scheme)], db=Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        cpf: str = payload.get("sub")
        if cpf is None:
            raise credentials_exception
        token_data = TokenData(cpf=cpf)
    except InvalidTokenError:
        raise credentials_exception
    account = await get_account_by_cpf(db, cpf=token_data.cpf)
    if account is None:
        raise credentials_exception
    return account


async def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
