from fastapi import APIRouter
from models.account import Account
from database import get_db
from fastapi import Depends
from typing import Annotated
from dependencies import get_current_account
from crud.position import get_positions_from_account
from schemas import PositionResponse

router = APIRouter(prefix="/positions")


@router.get("/healthcheck")
async def root():
    """
    Returns a JSON response with a message.
    """
    return {"message": "This is the positions router"}


@router.get("/my-positions")
async def get_positions(
    current_account: Annotated[Account, Depends(get_current_account)],
    session=Depends(get_db),
):
    """
    Show all positions of the current account.
    """

    positions_from_account = await get_positions_from_account(
        session, current_account
    )
    positions_response = PositionResponse.from_positions(
        positions_from_account, current_account.amount
        )

    return positions_response
