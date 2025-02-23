import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser
import wikipedia
from datetime import datetime
import pyjokes

# Função para converter fala em texto
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para ruído de fundo...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ouvindo...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender.")
        return ""
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de fala.")
        return ""

# Função para converter texto em fala
def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Função para responder aos comandos
def respond(command):
    if 'youtube' in command:
        speak("O que você quer pesquisar no YouTube?")
        query = get_audio()
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak(f"Aqui está o que encontrei sobre {query} no YouTube.")
    elif 'wikipedia' in command:
        speak("O que você quer pesquisar na Wikipedia?")
        query = get_audio()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2, lang='pt')
                speak("De acordo com a Wikipedia:")
                print(summary)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError:
                speak("Encontrei várias opções, tente ser mais específico.")
            except wikipedia.exceptions.PageError:
                speak("Não encontrei resultados para essa pesquisa.")
    elif 'piada' in command:
        joke = pyjokes.get_joke(language='pt')
        print(joke)
        speak(joke)
    elif 'horas' in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"Agora são {now}.")
    elif 'farmácia' in command:
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")
        speak("Aqui estão as farmácias próximas a você.")
    elif 'sair' in command:
        speak("Até mais!")
        exit()

# Loop principal
while True:
    print("Estou ouvindo...")
    user_command = get_audio()
    if user_command:
        respond(user_command)
