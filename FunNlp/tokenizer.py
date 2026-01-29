import os
import requests

class Tokenizer():
    def __init__(self):
        self.wordMap = {}
        self.wordMap2 = {}

    def format_text(self, t):
      t = t.replace(".", "").replace("?", "").replace("!", "")
      return t

    def build_vocab(self,file,fromWeb=False):
        self.wordMap = {}
        splitted = None
        if not fromWeb:
            with open(file, "r") as f:
                text = f.read()
                text = self.ormat_text
                splitted = text.split(' ')
        else:
            response = requests.get(file)
            response.raise_for_status()
            response.text = self.format_text(response.text)
            splitted = response.text.split(' ')

        for i in range(len(splitted)):
            if splitted[i].lower() not in self.wordMap:

              self.wordMap[splitted[i].lower()] = i
              self.wordMap2[i] = splitted[i].lower()

    def build_vocab_var(self, texts):
      combined_text = ""
      for j,text in enumerate(texts):
        combined_text += text

      combined_text = self.format_text(combined_text)
      splitted = combined_text.split(' ')
      for i in range(len(splitted)):
        if splitted[i].lower() not in self.wordMap:
          self.wordMap[splitted[i].lower()] = i
          self.wordMap2[i] = splitted[i].lower()


    def addToken(self, word):
        if word not in self.wordMap:
            self.wordMap[word] = len(self.wordMap)
            self.wordMap2[len(self.wordMap)] = word

    def encode(self, text):
        text = text.lower()
        text = self.format_text(text)

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