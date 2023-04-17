import pyttsx3
import speech_recognition as sr
from models.OpenLibrary import OpenLibrary
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
                print("IA: Voce disse '"+text+"'")
                SpeakText(text)
                match text:
                    case "buscar livro":
                        print("IA: Que livro voce deseja procurar?")
                        audio = recog.listen(mic)
                        text = recog.recognize_google(audio, language='pt-BR')
                        books = ol.search_books_by_title(text)
                        print(books)
                        response = helpers.create_list_books(books)
                    case "buscar autor":
                        print("IA: Que autor voce deseja procurar?")
                        audio = recog.listen(mic)
                        text = recog.recognize_google(audio, language='pt-BR')
                        response = ol.search_books_by_author(text)
                    case _:
                        print("IA: Não há função para '"+text+"'")
                        
                return response
                    

        except sr.RequestError as e:
            print("Não foi possivel requisitar o pedido; (0)".format(e))

        except sr.UnknownValueError:
            print("Um erro desconhecido ocorreu")