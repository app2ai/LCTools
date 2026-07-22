from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from currency_exchange import CurrencyExchange

load_dotenv()

chat_model = ChatOpenAI()

exchange_tool = CurrencyExchange()

chat_model_with_tool = chat_model.bind_tools([exchange_tool])

query = "Convert 10 USD to INR"

messages = [query]

tool_call_query_result = chat_model_with_tool.invoke(query)

# print(tool_call_query_result)
# content='' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 26,
# 'prompt_tokens': 88, 'total_tokens': 114, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0,
# 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None,
# 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 
# 'id': 'chatcmpl-E4UcSOzCO6lHyLO2dT84gM1TEH0gk', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}
# id='lc_run--019f8ac6-d5e6-7cb0-91af-e477af5c0bf6-0' tool_calls=[{'name': 'currency_exchanger', 'args': {'base_currency': 'EUR',
# 'target_currency': 'USD', 'conversion_value': 100}, 'id': 'call_h25pL4GCGTC9XFJR5LR6ALMC', 'type': 'tool_call'}]
# invalid_tool_calls=[] usage_metadata={'input_tokens': 88, 'output_tokens': 26, 'total_tokens': 114, 'input_token_details': 
# {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# Extract tool call only
# tool_calls=[{'name': 'currency_exchanger', 'args': {'base_currency': 'EUR',
# 'target_currency': 'USD', 'conversion_value': 100}, 'id': 'call_h25pL4GCGTC9XFJR5LR6ALMC', 'type': 'tool_call'}]

# append llm response with binding tool and human query
messages.append(tool_call_query_result)

currency_exchange_tool_response = exchange_tool.invoke(tool_call_query_result.tool_calls[0])

# print(currency_exchange_tool_response)
# This is result from Tool
# content='b\'{"success":true,"terms":"https:\\\\/\\\\/currencylayer.com\\\\/terms","privacy":"https:\\\\/\\\\/currencylayer.com
# \\\\/privacy","query":{"from":"EUR","to":"USD","amount":100},"info":{"timestamp":1784741105,"quote":1.141289},
# "result":114.1289}\'' name='currency_exchanger' tool_call_id='call_2HrCOVaSnbj6YH4aa3aZcrrD'

# append in messages
messages.append(currency_exchange_tool_response)

# Now finally execute llm_with_tool
final_result = chat_model_with_tool.invoke(messages).content

print(final_result)
# query = 'Convert 100 EUR to USD' : answer = '100 EUR is equivalent to 114.1032 USD.'
# query = 'Convert 10 USD to INR' : answer = '10 USD is equivalent to 965.51 INR.'