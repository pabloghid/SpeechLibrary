import pyttsx3
import speech_recognition as sr
from models.OpenLibrary import OpenLibrary
from models.Author import Author
import helpers

ol = OpenLibrary()

def SpeakText(command):
    out = pyttsx3.init()
    if(command != "desligar"):
        out.say(command)
    else:
        out.say("Ok! Estou desligando...")
    out.runAndWait()


def VoiceSearch():
    recog = sr.Recognizer()

    text = ""

    while(text != "desligar"):
        try:
            with sr.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic)
                print("IA: o que você quer fazer?")
                audio = recog.listen(mic)
                text = recog.recognize_google(audio, language='pt-BR')
                return text
                    

        except sr.RequestError as e:
            print("Não foi possivel requisitar o pedido; (0)".format(e))

        except sr.UnknownValueError:
            print("Um erro desconhecido ocorreu")

def search_book():
    text = VoiceSearch()
    books = ol.search_books_by_title(text)
    response = helpers.create_list_books(books)
    return response

def search_author():
    text = VoiceSearch()
    authors = ol.search_author(text)
    response = helpers.create_list_authors(authors)
    print(response)
    return response