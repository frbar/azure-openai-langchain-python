import os
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_DEPLOYMENT_NAME"] = "gpt-4-32k"

from langchain.chat_models import AzureChatOpenAI
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.callbacks import get_openai_callback

llm = AzureChatOpenAI(deployment_name="gpt-4-32k", 
                      openai_api_version="2023-05-15",
                      openai_api_key=os.environ["OPENAI_API_KEY"],
                      openai_api_base=os.environ["OPENAI_API_BASE"])

with get_openai_callback() as cb:
    chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)
    chain('What is the weather like right now in Bordeaux, France in degrees Celcius?')
    print(cb)
