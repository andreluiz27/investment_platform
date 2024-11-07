from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import relationship


class Position(Base):
    """
    Represents a position in a trading account.

    Attributes:
        id_position (int): The unique identifier for the position.
        acc_code (int): The account code associated with the position.
        symbol (str): The symbol of the position.
        amount (float): The amount of the position.
        last_price (float): The last price of the position.
        account (Account): The account associated with the position.

    """
    __tablename__ = "position"
    id_position = Column(Integer, primary_key=True, index=True)
    acc_code = Column(Integer, ForeignKey("account.acc_code"))
    symbol = Column(String(10))
    amount = Column(Float)
    last_price = Column(Float)

    account = relationship("Account", back_populates="positions")
