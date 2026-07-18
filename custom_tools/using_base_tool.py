from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Add(BaseModel):
    a: int = Field(required = True, description="Input number one")
    b: int = Field(required = True, description="Input number two")


class AddNumTool(BaseTool):

    name: str = "Addition"

    description : str = "Addition of 2 numbers"

    args_schema : Type[BaseModel] = Add

    def _run(self, a: int, b: int) -> int:
        return a+b

add = AddNumTool()
res = add.invoke({'a': 5, 'b': 6})
print(res)
print(add.args)

# Output
# 11
# {'a': {'description': 'Input number one', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'Input number two', 'title': 'B', 'type': 'integer'}}
