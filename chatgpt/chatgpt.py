# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

# def generate_response(input_text):
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")
#     response = model.generate(input_ids, max_length=100)[0]
#     response_text = tokenizer.decode(response, skip_special_tokens=True)
#     return response_text

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones_like(input_ids)
    pad_token_id = tokenizer.eos_token_id
    response = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=pad_token_id, max_length=100)[0]
    response_text = tokenizer.decode(response, skip_special_tokens=True)
    return response_text
