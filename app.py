from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly assistant for Indian farmers. Respond in simple and clear Hindi so that illiterate farmers can understand easily."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        reply = "माफ कीजिए, कुछ गलती हो गई।"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
