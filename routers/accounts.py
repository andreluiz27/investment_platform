from fastapi import APIRouter
from models.account import Account
from database import get_db
from fastapi import Depends
from typing import Annotated
from dependencies import get_current_account

router = APIRouter(prefix="/accounts")


@router.get("/healthcheck")
async def root():
    """
    Returns a JSON response with a message.
    """
    return {"message": "This is the accounts router"}


@router.get("/my-account")
async def get_account(
    current_account: Annotated[Account, Depends(get_current_account)],
    session=Depends(get_db),
):
    """
    Show the account details of the current user.
    """
    return current_account
