from pydantic import BaseModel, Field, validator
from decimal import Decimal, ROUND_HALF_UP


class AccountResponse(BaseModel):
    """
    Represents an account response.

    Attributes:
        acc_code (int): Code of the account.
        name (str): Name of the account.
        amount (float): Amount of the account.
    """

    acc_code: int = Field(
        ..., title="Account Code", description="Account's code", example=123456
    )
    name: str = Field(..., title="Name", description="Owner's name", example="John Doe")
    amount: float = Field(
        ..., title="Amount", description="Quantity of stock", example=1000.00
    )

    @classmethod
    def from_orm(cls, account):
        """
        Converts an ORM account object to a Pydantic AccountResponse object.

        Parameters:
        - account: The ORM account object.

        Returns:
        - The Pydantic AccountResponse object.
        """
        return cls(
            acc_code=account.acc_code,
            name=account.name,
            amount=float(account.amount),
        )

    @validator("amount")
    def ensure_two_decimal_places(cls, v):
        return Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
