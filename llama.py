from transformers import AutoTokenizer, AutoModelForCausalLM

def init_llama_model():
    model_name = "meta-llama/Llama-3.3-70B-Instruct"
    huggingface_token = "your token just send a request for llama 3.3"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=huggingface_token)
    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=huggingface_token)
    return tokenizer, model

def generate_response(tokenizer, model, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response