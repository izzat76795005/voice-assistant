import pyttsx3  # Library for text-to-speech synthesis
import datetime  # For working with current date and time
import speech_recognition as sr  # For speech recognition
import webbrowser  # For opening web pages in the browser
import requests  # For making HTTP requests (e.g., to fetch weather data)
import random  # For generating random values (not used in this code)
import wikipedia  # For retrieving information from Wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')  # Using SAPI5 text-to-speech engine (available on Windows)
voices = engine.getProperty('voices')  # Retrieve available voice options
engine.setProperty("voice", voices[1].id)  # Set the voice to female (index 1)

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)  # Pass text to the TTS engine
    engine.runAndWait()  # Execute speech synthesis

# Function to greet the user based on the time of day
def wish_me():
    hour = datetime.datetime.now().hour  # Get the current hour
    if 0 <= hour < 12:
        speak("Good morning!")  # Morning greeting
    elif 12 <= hour < 18:
        speak("Good afternoon!")  # Afternoon greeting
    else:
        speak("Good evening!")  # Evening greeting
    speak("I am Selena. How can I assist you today?")  # Introduce the assistant

# Function to listen for user commands
def take_command():
    recognizer = sr.Recognizer()  # Initialize the speech recognizer
    with sr.Microphone() as source:  # Use the microphone as the input source
        print("Listening...")
        recognizer.pause_threshold = 1  # Pause time before processing speech
        recognizer.adjust_for_ambient_noise(source)  # Reduce ambient noise for better accuracy
        audio = recognizer.listen(source)  # Capture audio from the microphone

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-US")  # Use Google's speech recognition
        print(f"User said: {query}\n")  # Print the recognized command
    except Exception as e:  # Handle errors during recognition
        print(e)
        speak("Sorry, I didn't catch that. Can you please repeat?")  # Prompt user to repeat
        return "None"  # Return "None" if recognition failed
    return query.lower()  # Return the recognized command in lowercase

# Function to fetch weather information
def get_weather(city):
    api_key = "1b8499c835bbcbe44c2ab0cec065cd65"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # API endpoint
    response = requests.get(url)  # Send an HTTP GET request to the API
    data = response.json()  # Parse the JSON response
    print(data)  # Debugging: Print the raw weather data
    if data["cod"] != "200":  # Check if the response is valid
        weather_desc = data["weather"][0]["description"]  # Extract weather description
        temperature = data["main"]["temp"]  # Extract temperature
        speak(f"The weather in {city} is {weather_desc}. The temperature is {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't find the weather for that location.")  # Handle invalid city names

# Main function to run the voice assistant
if __name__ == "__main__":  # Ensure this block runs only when the script is executed directly
    wish_me()  # Call the greeting function
    query = take_command()  # Get the user's command
    print("Query:", query)  # Debugging: Print the recognized query

    if 'open website' in query:  # Check if the command is to open a website
        speak("Which website would you like to open?")  # Ask for the website name
        website = take_command()  # Listen for the website name
        webbrowser.open(website + ".com")  # Open the website in the browser
    
    elif 'weather' in query:  # Check if the command is for weather
        print("Weather command recognized")  # Debugging: Print confirmation
        speak("Sure, please tell me the city name.")  # Prompt user for the city
        city = take_command()  # Listen for the city name
        print("City:", city)  # Debugging: Print the recognized city
        get_weather(city)  # Fetch and announce the weather

        engine = pyttsx3.init()  # Re-initialize the text-to-speech engine (this seems redundant)
