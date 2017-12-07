from chatterbot import ChatBot
from gtts import gTTS
from pygame import mixer
import random
import os
from random import randint
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")
print("I'm ready to talk")
lista=[]
while(1):
    name=""
    name=name+str(randint(0, 9999))+str(randint(0, 9999))+".mp3"
    blabla="Ye bolke dikha"
#blabla=input()
    blabla=str(input())
    if(blabla=="exit"):
        string=["It was nice talking to you :)","You bored me.:("][random.randint(0,1)]
        print(string)
        break

# Get a response to an input statement
    abc=chatbot.get_response(blabla)
    tts=gTTS(text=str(abc),lang='en')
    tts.save(name)
    lista.append(name)
    print(str(abc))
    mixer.init()
    mixer.music.load(name)
   
    mixer.music.play()
for i in lista:
    os.remove(i)
