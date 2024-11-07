from pydantic import BaseModel, Field, validator
from decimal import Decimal, ROUND_HALF_UP


class AccountResponse(BaseModel):
    acc_code: int = Field(
        ..., title="Account Code", description="Code of the account", example=123456
    )
    name: str = Field(
        ..., title="Name", description="Name of the account", example="John Doe"
    )
    amount: float = Field(
        ..., title="Amount", description="Amount of the account", example=1000.00
    )

    @validator("amount")
    def ensure_two_decimal_places(cls, v):
        return Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
