import platform
# import pyaudio
import speech_recognition as sr
import nltk
from nltk.stem import WordNetLemmatizer
# from nltk import tokenize as tk
from nltk.corpus import stopwords, wordnet
# from operator import itemgetter
# import math
# import pocketsphinx
import sys
import vosk
import json
from vosk import SetLogLevel
from os import path
from time import time

SetLogLevel(-1)
# nltk.download("averaged_perceptron_tagger")
# nltk.download("punkt")
# nltk.download("wordnet")

p = platform.system()
class Speech2Command:

    def __init__(self, mode=None, data=None, loc=None, src=None):
        self.mode = mode
        self.loc = loc
        self.src = src
        self.cmd = None
        self.data = data

    def listen(self):
        rec = sr.Recognizer()
        if self.mode == "mic":
            with sr.Microphone() as src:
                rec.adjust_for_ambient_noise(src)
                audio = rec.listen(src)
        elif self.mode == "rec":
            if __name__ == "__main__":
                with sr.AudioFile(self.loc) as src:
                    audio = rec.record(src)
            else:
                audio = rec.record(self.data)  # self.data
        try:
            if self.src == 'vosk':
                self.cmd = rec.recognize_vosk(audio_data=audio)  # language="en-in")
            elif self.src == 'google':
                self.cmd = rec.recognize_google(audio_data=audio) # language="en-in")
            # print(f"Command: {cmd}")
        except Exception:
            print("Sorry, couldn't hear. Mind trying typing it?")
            self.cmd = input()
        # cmd=cmd.split(" ")
        # self.splitcmd = self.cmd.split(" ")
        return self.cmd

    # def psphinx(self):
    #     sp = pocketsphinx.LiveSpeech()
    #     return sp

    def pos_tagger(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    def lemmatizer(self, src):
        w = WordNetLemmatizer()
        pos_tagged = nltk.pos_tag(nltk.word_tokenize(src))
        wn_tagged = list(map(lambda x: (x[0], self.pos_tagger(x[1])), pos_tagged))
        ls = []  # lemmatized sentence
        for word, tag in wn_tagged:
            if tag is None:
                ls.append(word)
            else:
                ls.append(w.lemmatize(word, tag))
        return ls

    def make_tokens(self, lms):
        stop_words = set(stopwords.words('english')) # +['Maryam']-['ok'])
        src3 = []
        for i in lms:
            if i in stop_words:
                pass
            else:
                src3.append(str(i)+" ")
        print("Keywords are:", end=' ')
        for i in src3:
            print(i, end=' ')
        print("\n\n")
    
    def save(self, data):
        f = open(f"output {time()}.txt", "a")
        f.write(data)

    def exec(self):
        # if self.mode == "mic":
        try:
            while True:
                # print("\nSay some words: ")
                c = self.listen()
                print("Listened value=",c)
                if self.src == 'vosk':
                    d = json.loads(c)
                    self.cmd = d["text"]
                elif self.src == 'google':
                    self.cmd = c
                    print("Command =", self.cmd)
                
                if str(self.cmd.rstrip(" ")) in ['stop', 'exit', 'bye', 'quit', 'terminate', 'kill', 'end']:
                    print("\n\nExit command triggered from command! Exiting...")
                    sys.exit()
                # lemmatized = self.lemmatizer(self.cmd)
                # self.make_tokens(lemmatized)
                self.save(self.cmd)
                if self.mode == "rec":
                    break
        except KeyboardInterrupt:
            print("\n\nExit command triggered from Keyboard! Exiting...")
        # elif self.mode == "rec":
        #     try:
        #         print("\nListening to the audio you supplied...")
        #         c = listen()
        #         print("Listened value=",c)
        #         d = json.loads(c)
        #     except KeyboardInterrupt:
        #         print("\n\nExit command triggered from Keyboard! Exiting...")

def driver(mode=None, translator=None, location=None, data=None):
    loc = location
    source = translator
    mode = mode
    data = data
    if __name__ == "__main__":
        while True:
            mode = input("Enter mode: ('mic' for microphone or 'rec' for recording)\n")
            print("\n")
            if mode == 'mic':
                break
            elif mode == 'rec':
                while True:
                    loc = input("Enter file location:\n")
                    print("\n")
                    if path.exists(loc):
                        break
                    else:
                        print("\nFile doesn't exist. Try again.\n")
                        continue
                break
            else:
                print("\nInvalid mode.Try again\n")

        while True:
            source = input("Enter translator: ('vosk' for Vosk or 'google' for Google)\n")
            print("\n")
            if source == 'google':
                break
            elif source == 'vosk':
                break
            else:
                print("\nInvalid translator.Try again\n")
            
    instance = Speech2Command(mode=mode, loc=loc, src=source, data=data)
    output = instance.exec()

    return output

if __name__ == '__main__':
    print(driver())