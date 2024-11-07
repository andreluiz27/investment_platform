from typing import Union
from pydantic import BaseModel


class Token(BaseModel):
    """
    Represents a token object.

    Attributes:
        access_token (str): The access token.
        token_type (str): The type of the token.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Represents the data contained in a token.

    Attributes:
        cpf (Union[str, None]): The CPF  associated with the token.
    """
    cpf: Union[str, None] = None
