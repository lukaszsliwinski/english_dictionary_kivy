from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

import csv, random

# Create dictionary from csv file
with open('dictionary.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    dictionary = {rows[0]:rows[1:] for rows in reader}
    for value in dictionary.values():
        i = 0
        while i < len(value):
            if value[i] == '':
                del value[i]
                continue
            i += 1


# Choose random polish words to translate and save to list
pl_words = []
i=0
while i < 3:
    random_word = random.choice(list(dictionary))
    if random_word not in pl_words:
        pl_words.append(random_word)
        i+=1




class Card(Screen):
    id = int()
    word = StringProperty()
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.word = pl_words[self.id]

    def check(self):
        input = self.ids["input"+str(self.id+1)].text
        self.ids["input"+str(self.id+1)].readonly = True
        if input in list(dictionary[self.word]) or input == dictionary[self.word]:
            print("correct")
            print(list(dictionary[self.word]))
        else:
            print("incorrect")
            print(list(dictionary[self.word]))




class Card1(Card):
    id = 0

class Card2(Card):
    id = 1

class Card3(Card):
    id = 2






gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        return gui

if __name__ == '__main__':
    EnglishApp().run()
