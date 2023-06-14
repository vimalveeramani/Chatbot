# Import necessary libraries

from flask import Flask, render_template, request

import requests

app = Flask(__name__)

# Routes

@app.route('/')

def index():

    # Render the home page with the dropdowns

    return render_template('index.html')

@app.route('/chat', methods=['POST'])

def chat():

    # Extract the selected health condition and severity from the form data

    condition = request.form.get('condition')

    severity = request.form.get('severity')

    # Construct the message for the ChatGPT API request

    message = f"Condition: {condition}, Severity: {severity}"

    # Make a POST request to the ChatGPT API with the message payload

    headers = {

        'Authorization': 'Bearer YOUR_API_KEY',

        'Content-Type': 'application/json',

    }

    data = {

        'messages': [{'role': 'system', 'content': 'You are a user'}, {'role': 'user', 'content': message}]

    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    chat_response = response.json()['choices'][0]['message']['content']

    # Return the chatbot's response

    return chat_response

if __name__ == '__main__':

    app.run(debug=True)

