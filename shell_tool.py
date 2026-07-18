from langchain_community.tools import ShellTool
from dotenv import load_dotenv

load_dotenv()

shell = ShellTool()
res = shell.invoke('mkdir langchainTest')
print(res)
