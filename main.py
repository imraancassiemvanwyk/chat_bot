from huggingface_hub import InferenceApi
from flask import Flask, request, jsonify


inference = InferenceApi(repo_id="meta-llama/Llama-2-7b-chat-hf" ,
                         token="your own token from hugging face")
app = Flask(__name__)
chat_history = []

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_input = request.json.get("user_input", "")

    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    chat_history.append({"role": "user", "content": user_input})
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
    try:
        response = inference(inputs=context)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    bot_response = response.get("generated_text", "").strip()

    chat_history.append({"role": "assistant", "content": bot_response})

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
