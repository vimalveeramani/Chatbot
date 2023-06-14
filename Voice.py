from gtts import gTTS

import os

@app.route('/chat', methods=['POST'])

def chat():

    # ...

    # Return the chatbot's response

    chat_response = response.json()['choices'][0]['message']['content']

    # Convert the chatbot's response to voice using gTTS

    tts = gTTS(text=chat_response, lang='en')

    tts.save('response.mp3')

    os.system('mpg321 response.mp3')  # Install mpg321 or use another audio player command

    # Return the chatbot's response and embed an audio player in the template

    return render_template('response.html', chat_response=chat_response)

