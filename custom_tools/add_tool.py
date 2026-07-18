from langchain_community.tools import tool

# Tool for add 2 numbers
@tool
def add(a:int, b:int) -> int:
    """Add two numbers"""
    return a+b