from langchain_community.tools import DuckDuckGoSearchResults
from dotenv import load_dotenv

load_dotenv()

duck = DuckDuckGoSearchResults()

result = duck.invoke('Todays gold rate?')

print(result)
