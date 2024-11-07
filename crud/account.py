from sqlalchemy.orm import Session

from models.account import Account


async def get_account_by_acc_code(db: Session, acc_code: int):
    """
    Retrieve an account from the database based on the account code.

    Args:
        db (Session): The database session.
        acc_code (int): The account code.

    Returns:
        Account: The account object matching the account code, or None if not found.
    """
    return db.query(Account).filter(Account.acc_code == acc_code).first()


async def get_account_by_cpf(db: Session, cpf: str):
    """
    Retrieve an account from the database based on the provided CPF.

    Args:
        db (Session): The database session.
        cpf (str): The CPF of the account to retrieve.

    Returns:
        Account: The account object matching the provided CPF, or None if not found.
    """
    return db.query(Account).filter(Account.cpf == cpf).first()
