from langchain_core.tools import BaseTool
from typing import Type
from currency_args import CurrencyModel
from exchange_api import fetchCurrency

class CurrencyExchange(BaseTool):
    name: str = 'currency_exchanger'
    description: str = 'Find rate factor between 2 currency and gave value'
    args_schema: Type[CurrencyModel] = CurrencyModel

    def _run(self, base_currency, target_currency, conversion_value) -> int:
        response = fetchCurrency(self=self, base=base_currency, target=target_currency, value=conversion_value)
        return response

        