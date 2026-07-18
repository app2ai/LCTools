from math_toolkit import MathToolKit

math_tools = MathToolKit()
tools = math_tools.get_tools()

for tool in tools:
    print(tool.name)