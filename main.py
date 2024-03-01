import PyPDF2
import gtts.lang
from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import pyttsx3
translator = Translator()
print("\tUse code of your preferred language from the following list:\t")
print(gtts.lang.tts_langs())
b = input("Enter the pdf name")
book = open(b, 'rb')
s = input("Enter the language of pdf")
dest = input("Enter the language in which you want to read pdf")
pdfReader = PyPDF2.PdfReader(book)
print("Total pages", len(pdfReader.pages))
p = int(input("Enter the page no you want to read"))
speaker = pyttsx3.init()
for num in range(p, len(pdfReader.pages)):
    pages = pdfReader.pages[p]
    text = pages.extract_text()
    result = translator.translate(text=text, src=s, dest=dest)
    print(result.src)
    print(result.dest)
    print(result.origin)
    print(result.pronunciation)
    tts = gTTS(text=result.text, lang=dest, slow=False)
    audio = "speech.mp3"
    tts.save(audio)
    playsound(audio)
