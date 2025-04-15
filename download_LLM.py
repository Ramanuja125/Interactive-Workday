from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "tensoropera/Fox-1-1.6B-Instruct-v0.1"

# Download model
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Model and tokenizer downloaded successfully!")