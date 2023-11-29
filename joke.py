import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks import get_openai_callback

openai_api_key = os.environ['OPENAI_API_KEY']
openai_api_base = os.environ['OPENAI_API_BASE']

llm = AzureChatOpenAI(deployment_name="gpt-4-32k", 
                      openai_api_version="2023-05-15", 
                      openai_api_key=openai_api_key, 
                      openai_api_base=openai_api_base)

msg = HumanMessage(content="Tell me a random joke about cars")

with get_openai_callback() as cb:
    print(llm(messages=[msg]))
    print(cb)