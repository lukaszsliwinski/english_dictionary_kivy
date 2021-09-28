from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
# from kivy.clock import mainthread

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
i = 0
while i < 3:
    random_word = random.choice(list(dictionary))
    if random_word not in pl_words:
        pl_words.append(random_word)
        i += 1



class Card(Screen):
    id = int()
    word = StringProperty()
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.word = pl_words[self.id]

    def check(self):
        input = self.ids[f'input{str(self.id+1)}'].text
        correct_counter = int(self.ids[f'result{str(self.id+1)}'].text)
        self.ids[f'input{str(self.id+1)}'].readonly = True

        answer = ''
        
        if len(dictionary[self.word]) == 1:
            answer = f'{dictionary[self.word][0]}'
        else:
            for translation in dictionary[self.word]:
                answer += f'{str(i+1)}. {translation}'
                answer += '\n'
        if input in list(dictionary[self.word]) or input == dictionary[self.word]:
            self.ids[f'answer{str(self.id+1)}'].text = f'correct\n{answer}'
            correct_counter += 1
            self.ids[f'result{str(self.id+1)}'].text = f'{correct_counter}'
        else:
            self.ids[f'answer{str(self.id+1)}'].text = f'incorrect\n{answer}'

    def pass_result(self):
        try:
            self.manager.get_screen(f'card{str(self.id+2)}').ids[f'result{str(self.id+2)}'].text \
            = self.manager.get_screen(f'card{str(self.id+1)}').ids[f'result{str(self.id+1)}'].text
        except:
            pass
            # W tym miejscu dodać przesłanie liczby poprawnych odpowiedzi na kartę kończącą program
#
#
#
#
#
#
#
#
#
# UWAGA! We wszystkich funkcjach ze zmiennymi po self.id należy dodać warunki brzegowe
# Możliwe błędy przy ostatniej karcie

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
