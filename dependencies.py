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
    """
    Authenticates a user by checking if the provided CPF and password match an
    existing account.

    Args:
        cpf (str): The CPF (Brazilian identification number) of the user.
        password (str): The password of the user.
        db: The database connection object.

    Returns:
        Union[bool, Account]: Returns the account object if the authentication
         is successful, otherwise returns False.
    """
    account = await get_account_by_cpf(db, cpf)
    if not account:
        return False
    if not verify_password(password, account.hashed_password):
        return False
    return account


async def get_current_account(
    token: Annotated[str, Depends(oauth2_scheme)],
    db=Depends(get_db)
):
    """
    Retrieves the current account based on the provided token.

    Args:
        token (str): The authentication token.
        db: The database dependency.

    Returns:
        The current account.

    Raises:
        HTTPException: If the credentials cannot be validated.
    """

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


async def create_access_token(
    data: dict,
    expires_delta: Union[timedelta, None] = None
 ):
    """
    Create an access token with the given data and expiration delta.

    Args:
        data (dict): The data to be encoded in the access token.
        expires_delta (Union[timedelta, None], optional): The expiration delta
        for the access token.
            If not provided, a default expiration of 15 minutes will be used.

    Returns:
        str: The encoded access token.

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
