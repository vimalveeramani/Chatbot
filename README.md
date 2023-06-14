

# Python Web App with Flask and ChatGPT API Integration

This is a Python web application built with Flask that integrates the ChatGPT API to create a chatbot capable of responding based on the selected health condition and severity.

## Features

- Dropdown menus to select the health condition and severity.
- Integration with the ChatGPT API to generate responses based on user input.
- Display of chatbot responses in the web interface.
- Optional text-to-speech functionality using the gTTS library.

## Prerequisites

- Python 3.x
- Flask (Install using `pip install flask`)
- Requests library (Install using `pip install requests`)
- ChatGPT API key (Obtain from OpenAI)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a ChatGPT API key from OpenAI.

4. Open the `app.py` file and replace `'YOUR_API_KEY'` with your actual ChatGPT API key.

## Usage

1. Start the Flask development server:

   ```bash
   python app.py
   ```

2. Open your web browser and visit `http://localhost:5000` to access the web app.

3. Select the health condition and severity from the dropdown menus.

4. Click the "Chat" button to send the request and view the chatbot's response.

## Additional Configuration (Optional)

To enable voice functionality using gTTS (Google Text-to-Speech):

1. Install the gTTS library:

   ```bash
   pip install gTTS
   ```

2. Uncomment the voice-related code sections in `app.py`.

3. Install `mpg321` or another audio player command to play the generated audio file.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [ChatGPT](https://platform.openai.com/docs/guides/chat) - OpenAI ChatGPT API
- [gTTS](https://gtts.readthedocs.io/en/latest/) - Google Text-to-Speech library






