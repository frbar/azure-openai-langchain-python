import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

openai_api_key = os.environ['OPENAI_API_KEY']
openai_api_base = os.environ['OPENAI_API_BASE']

llm = AzureChatOpenAI(deployment_name="gpt-4-32k", 
                      openai_api_version="2023-05-15", 
                      openai_api_key=openai_api_key, 
                      openai_api_base=openai_api_base)

msg = HumanMessage(content="Tell me a random joke about cars")
print(llm(messages=[msg]))