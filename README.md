Selena - Voice Assistant
Selena is a simple, customizable voice assistant built in Python. It is capable of handling basic voice commands such as opening websites, fetching weather information, and providing information from Wikipedia. This project serves as a great starting point for anyone interested in working with voice recognition, speech synthesis, and APIs.

Features
Voice Commands: Uses Google Speech Recognition to listen for user input.
Weather Information: Retrieves weather data using the OpenWeatherMap API.
Website Opening: Opens websites based on voice commands.
Text-to-Speech: Uses pyttsx3 to convert text responses into speech.
Future Multilingual Support: I plan to expand the assistant's capabilities by adding support for multiple languages, allowing users from different regions to interact with the assistant in their native language.
Requirements
Python 3.8
Required Python libraries:
pyttsx3 for text-to-speech
speech_recognition for voice command input
requests for fetching weather data
wikipedia for retrieving information from Wikipedia (optional)
webbrowser for opening websites
You can install the required libraries using pip:

pip install pyttsx3 SpeechRecognition requests wikipedia
Usage
Clone or download this repository to your local machine.
Ensure your microphone is set up and functioning.
Run the Python script:
python assistant.py
Once the script is running, you can issue commands like:

"Open website [website_name]"
"What's the weather in [city]?"
The assistant will respond with either a spoken reply or by opening the requested website.

Important Note
VS Code: The voice assistant works well in Visual Studio Code.
PyCharm: Currently, the voice assistant does not work properly in PyCharm. There is a known issue where the microphone input and speech recognition components may not work as expected. Therefore, it is highly recommended to use VS Code for running this project.
How It Works
Initialization: The voice assistant is initialized using pyttsx3 for speech synthesis.
Greeting: The assistant greets you based on the time of day.
Speech Recognition: The assistant listens to your voice commands using speech_recognition.
Command Handling: The assistant checks the command and performs an action (e.g., opening a website or fetching weather information).
Weather Information: The assistant fetches weather data using the OpenWeatherMap API and speaks the weather conditions aloud.
Acknowledgements
I would like to express my sincere thanks to Avi Upadhyay for his amazing tutorials on building voice assistants. His videos provided me with the initial knowledge and motivation to create this project. While following his guidance, I added my own features such as weather information and noise reduction for better voice recognition. Avi's content was crucial to the development of this voice assistant, and I deeply appreciate the value of his educational resources.

Future Improvements
Website Integration: I plan to integrate the voice assistant directly into websites, allowing users to interact with websites through voice commands. This feature is something I have not seen implemented elsewhere, and I believe it would add a unique functionality.
More Commands: I am looking to add more features such as setting reminders, playing music, and providing more detailed answers from Wikipedia.
Multilingual Support: I plan to add support for multiple languages in the future, enabling a broader audience to interact with the assistant in their native language.
License
This project is licensed under the MIT License - see the LICENSE file for details.

By using this code, you agree to mention the author [Your Name] in any derivative works or if you plan to distribute or use it for commercial purposes.

Contributing
I am open to suggestions and future improvements. If you have any ideas or want to contribute, feel free to fork this repository and submit a pull request. Please provide feedback, report bugs, or suggest new features via GitHub Issues.

Important:
If you use or modify this code, please credit me by mentioning [Your Name] in your project or documentation.
Updates:
VS Code and PyCharm Compatibility: Added a clear note that the voice assistant does not work properly in PyCharm and works best in VS Code.
Multilingual Support: Added a note about the future plan to support multiple languages, allowing for a more global user base.
Acknowledgement: Added a special mention to Avi Upadhyay for providing inspiration and guidance through his YouTube tutorials
