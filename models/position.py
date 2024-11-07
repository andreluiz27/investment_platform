from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import relationship


class Position(Base):
    __tablename__ = "position"
    id_position = Column(Integer, primary_key=True, index=True)
    acc_code = Column(Integer, ForeignKey("account.acc_code"))
    symbol = Column(String(10))
    amount = Column(Float)
    last_price = Column(Float)

    account = relationship("Account", back_populates="positions")
