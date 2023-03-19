import speech_recognition as sr  # recognize speech input
import pyttsx3  # text-to-speech conversion
import webbrowser  # open web pages
import wikipedia  # retrieve information from wikipedia

# speech engine initialized
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 : male,1 : female
activationWord = "computer"  # 1 word
# specify the browser
# chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


# speaking method
def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


# listening for commands
def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source, duration=1)
        input_speech = listener.listen(source)
    try:
        print('Recognizing speech...')
        # Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
        query = listener.recognize_google(input_speech, language='en_us')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        # say it out loud
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    return query


def search_wikipedia(keyword=''):
    """Searches for a page on Wikipedia with the given keyword and returns its summary."""
    searchResults = wikipedia.search(keyword)

    if not searchResults:
        return 'No result received'

    try:
        wikiPage = wikipedia.page(searchResults[0], auto_suggest=False)
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    wikiSummary = str(wikiPage.summary)
    return wikiSummary


# main loop
if __name__ == '__main__':
    speak('Welcome , how can I help you')

    while True:
        # parse command
        query = parseCommand().lower().split()  # list of word said
        if query[0] == activationWord:
            query.pop(0)

            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings everyone')
                else:  # whatever you are saying
                    query.pop(0)  # remove say
                    speech = ' '.join(query)
                    speak(speech)

            if query[0] == 'go' and query[1] == 'to':
                speak('Opening..')
                query = ''.join(query[2:])
                webbrowser.get('chrome').open_new(query)

            # wikipedia
            if query[0] == 'search':
                query = ''.join(query[1:])
                speak('Querying wikipedia')
                speak(search_wikipedia(query))

            if query[0] == 'goodbye':
                speak("See you later.")
                break
