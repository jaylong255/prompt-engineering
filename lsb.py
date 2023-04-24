import openai
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Set up the LLMS
llms = OpenAI(model_name="text-davinci-003", temperature=0)

# Set up the prompt

