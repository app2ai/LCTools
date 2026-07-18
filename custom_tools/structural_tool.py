from langchain_core.tools import StructuredTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class AddNums(BaseModel):
    a: int = Field(required = True, description="input number 1")
    b: int = Field(required = True, description="input number 2")


def add(a: int, b: int) -> int:
    return a+b

structuredTool = StructuredTool.from_function(
    func=add,
    name="Addition",
    description="Add 2 numbers",
    args_schema=AddNums
)

res = structuredTool.invoke({'a': 6, 'b':3})

print(res)
print(structuredTool.name)
print(structuredTool.description)
