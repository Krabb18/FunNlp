import os
import requests

class Tokenizer():
    def __init__(self):
        self.wordMap = {}
        self.wordMap2 = {}

    def build_vocab(self,file,fromWeb=False):
        self.wordMap = {}
        splitted = None
        if not fromWeb:
            with open(file, "r") as f:
                text = f.read()
                splitted = text.split(' ')
        else:
            response = requests.get(file)
            response.raise_for_status()
            splitted = response.text.split(' ')

        for i in range(len(splitted)):
            splitted[i] = splitted[i].replace(".", "")
            splitted[i] = splitted[i].replace("?", "")
            splitted[i] = splitted[i].replace("!", "")
            self.wordMap[splitted[i].lower()] = i
            self.wordMap2[i] = splitted[i].lower()
            
                
            

    def addToken(self, word):
        if word not in self.wordMap:
            self.wordMap[word] = len(self.wordMap) + 1
            self.wordMap2[len(self.wordMap) + 1] = word

    def encode(self, text):
        text = text.lower()
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        encoded_list = []
        splitted_text = text.split()
        for token in splitted_text:
            encoded_list.append(self.wordMap[token])
        return encoded_list

    def decode(self, tokens):
        decoded_list = []
        for token in tokens:
            decoded_list.append(self.wordMap2[token])
        return decoded_list
    
    def test(self,url):
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    