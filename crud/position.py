from sqlalchemy.orm import Session

from models.account import Account


async def get_positions_from_account(db: Session, account: Account):
    return account.positions
