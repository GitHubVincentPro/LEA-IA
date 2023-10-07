# Dans chatbot/model.py

import torch
from transformers import AutoModelForCausalLM

class Chatbot:

def __init__(self):
self.model = AutoModelForCausalLM.from_pretrained("gpt2")

def predict(self, conversation):
input_ids = self.preprocess(conversation)
outputs = self.model.generate(input_ids)
return outputs