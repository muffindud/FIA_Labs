import torch
import torch.nn as nn
from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("t5-small")

class Seq2SeqModel(nn.Module):
    def __init__(self, model_name="t5-small"):
        super(Seq2SeqModel, self).__init__()
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def forward(self, input_ids, attention_mask, labels):
        return self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)

model = Seq2SeqModel()
model.load_state_dict(torch.load('models/model20.pth'))

def generate_answer(question):
    model.eval()
    input_ids = tokenizer(question, return_tensors="pt").input_ids
    output = model.model.generate(input_ids)
    return tokenizer.decode(output[0], skip_special_tokens=True)
