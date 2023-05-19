from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

classifier = pipeline("sentiment-analysis")
# print(classifier("I've been waiting for a HuggingFace course my whole life!"))

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

for step in range(5):
    new_user_input_ids = tokenizer.encode(tokenizer.eos_token + input(">>User:"), return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim = 1) if step > 0 else new_user_input_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))