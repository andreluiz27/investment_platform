from schemas import Token
from database import get_db
from fastapi import Depends
from fastapi import APIRouter
from datetime import timedelta
from fastapi import HTTPException, status
from constants import ACCESS_TOKEN_EXPIRE_MINUTES
from dependencies import authenticate_user, create_access_token

from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth")


@router.post("/token")
async def login_for_access_token(
    form: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)
) -> Token:
    """
    Authenticates a user and generates an access token.

    Args:
        form (OAuth2PasswordRequestForm): The form containing the username
        and password.

        db: The database connection.

    Returns:
        Token: The generated access token.

    Raises:
        HTTPException: If the username or password is incorrect.
    """
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
