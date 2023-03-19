# AI Virtual Assistant

This is a voice-controlled assistant program that can perform various tasks using natural language processing and other tools. It is built in Python and utilizes libraries such as SpeechRecognition, Pyttsx3, Webbrowser, Wikipedia.

- The first library used is **`speech_recognition`**, which allows the program to recognize speech input from various sources like microphones. It provides an easy-to-use API to access speech recognition functionality from Google.
- The second library is **`pyttsx3`**, which enables the program to convert text to speech.
- The third library is **`webbrowser`**, which can open web pages.
- The fourth library is **`wikipedia`**, which the program uses to retrieve information from Wikipedia.

The script initializes the speech engine and sets its voice and activation word. It also registers the Chrome browser to use it to open web pages.

- **`speak(text, rate=120)`**: This function takes text as input and converts it to speech using **pyttsx3** library. The rate of speech can be adjusted using the optional rate parameter.
- **`parseCommand()`**: This function listens to the user's voice command using the microphone, recognizes the speech using the **Google Speech Recognition API**, and returns the recognized text. If the speech cannot be recognized, it returns "None".
- **`search_wikipedia(keyword='')`**: This function searches for a page on Wikipedia with the given **keyword** and returns its **summary**. It first searches for the given keyword, and if there are multiple results, it selects the first one. If there are disambiguation pages, it selects the first option.
- **`main`**: The main function starts with a welcome message and then listens to user's commands using **`parseCommand()`** function. When the user says the activation word (in this case, "**computer**"), the script checks for the type of command by splitting the input speech into a list of word and execute the specific command. The program can perform three actions:
- Say a message aloud by using "**say**" command.
- Open a webpage by using "**go to**" command.
- Search for a topic on Wikipedia by using "**search**" command. Once a topic is found, the program will speak its summary.