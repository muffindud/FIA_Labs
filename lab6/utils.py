import torch
import torch.nn as nn
from transformers import AutoTokenizer, T5ForConditionalGeneration

MODEL = 't5-base'
TRAINED_MODEL = 'model10base.pth'

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(MODEL)

class Seq2SeqModel(nn.Module):
    def __init__(self, model_name=MODEL):
        super(Seq2SeqModel, self).__init__()
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def forward(self, input_ids, attention_mask, labels):
        return self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)

model = Seq2SeqModel().to(device)
model.load_state_dict(torch.load(f'models/{TRAINED_MODEL}'))

def check_tokens(tokens):
    saved_tokens = torch.load('models/used_tokens.pt')['input_ids']
    return all([t in saved_tokens for t in tokens])

def generate_answer(question: str) -> str:
    model.eval()
    input_ids = tokenizer(question, return_tensors="pt").input_ids.to(device)

    if not check_tokens(input_ids[0]):
        unknown_words = []
        for token in input_ids[0]:
            if not check_tokens([token]):
                unknown_words.append(tokenizer.decode(token))
        return f"Sorry, I don't know the answer to the question. I don't know the meaning of the word(s): {', '.join(unknown_words)}."

    output = model.model.generate(input_ids)

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    if decoded == '':
        return "Sorry, I don't know the answer to that question."

    if decoded[-1].isalnum():
        decoded += '.'

    return decoded
