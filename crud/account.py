from sqlalchemy.orm import Session

from models.account import Account


async def get_account_by_acc_code(db: Session, acc_code: int):
    return db.query(Account).filter(Account.acc_code == acc_code).first()


async def get_account_by_cpf(db: Session, cpf: str):
    return db.query(Account).filter(Account.cpf == cpf).first()
