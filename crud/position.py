from sqlalchemy.orm import Session

from models.account import Account


async def get_positions_from_account(db: Session, account: Account):
    """
    Retrieve the positions associated with the given account.

    Parameters:
    - db (Session): The database session.
    - account (Account): The account object.

    Returns:
    - List[Position]: The positions associated with the account.
    """
    return account.positions
