from pydantic import BaseModel, Field, validator
from external_services.stocks import get_stock_price
from decimal import Decimal, ROUND_HALF_UP


class PositionSchema(BaseModel):
    symbol: str = Field(
        ..., title="Symbol", description="Symbol of the position", example="AAPL"
    )
    amount: float = Field(
        ..., title="Amount", description="Amount of the position", example=1000.00
    )
    current_price: float = Field(
        ...,
        title="Current Price",
        description="Current price of the position",
        example=100.00,
    )

    @validator("current_price")
    def ensure_two_decimal_places(cls, v):
        return Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class PositionResponse(BaseModel):
    positions: list[PositionSchema] = Field(
        ..., title="Positions", description="List of positions"
    )
    account_amount: float = Field(
        ...,
        title="Account Amount",
        description="Amount of the account",
        example=1000.00,
    )
    consolidated_amount: float = Field(
        ...,
        title="Consolidated Amount",
        description="Consolidated amount",
        example=1000.00,
    )

    @validator("account_amount")
    def ensure_two_decimal_places(cls, v):
        return Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @validator("consolidated_amount")
    def ensure_two_decimal_places(cls, v):
        return Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @classmethod
    def from_positions(cls, positions, account_amount):
        positions_schemas = []
        acumulated_amount = 0
        for position in positions:
            try:
                current_price = get_stock_price(position.symbol)
            except Exception as e:
                print(e)
                current_price = position.last_price

            positions_schemas.append(
                PositionSchema(
                    symbol=position.symbol,
                    amount=position.amount,
                    current_price=current_price,
                )
            )
            acumulated_amount += position.amount * current_price
        return cls(
            positions=positions_schemas,
            account_amount=account_amount,
            consolidated_amount=acumulated_amount,
        )
