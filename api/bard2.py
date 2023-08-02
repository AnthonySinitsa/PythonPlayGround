from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BARD_API_KEY")

bard = Bard(token = token)

input_text = "write a python function that adds 2 numbers together"

response = bardapi.core.Bard(token).get_answer(input_text)