from database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped

from models.position import Position

class Account(Base):
    __tablename__ = "account"
    acc_code = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    cpf = Column(String(11))
    amount = Column(Float)
    hashed_password = Column(String(255))

    positions = relationship("Position", back_populates="account")
