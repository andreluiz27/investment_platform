from database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Account(Base):
    """
    Represents a user account in the system.

    Attributes:
        acc_code (int): The account code.
        name (str): The name of the account holder.
        cpf (str): The CPF of the account holder.
        amount (float): The amount of money in the account.
        hashed_password (str): The hashed password for the account.
        positions (list): A list of positions associated with the account.
    """
    __tablename__ = "account"
    acc_code = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    cpf = Column(String(11))
    amount = Column(Float)
    hashed_password = Column(String(255))

    positions = relationship(
        "Position",
        back_populates="account"
    )
