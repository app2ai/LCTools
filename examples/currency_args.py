from pydantic import BaseModel, Field

class CurrencyModel(BaseModel):
    base_currency: str = Field(required = True, description='Input Base currency name')
    target_currency: str = Field(required = True, description='Input Target currency name')
    conversion_value: int = Field(required = True, description='Input exchange value number between currencies')
    