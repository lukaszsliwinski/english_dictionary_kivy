from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.core.window import Window


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
while i < 20:
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
        self.word_label = str(self.id+1) + ". " + self.word

    def check(self):
        input = self.ids[f'input{str(self.id+1)}'].text
        correct_counter = int(self.ids[f'score{str(self.id+1)}'].text)
        self.ids[f'input{str(self.id+1)}'].readonly = True

        answer = ''
        
        # Generate correct answer
        if len(dictionary[self.word]) == 1:
            answer = f'{dictionary[self.word][0]}'
        else:
            for i in range(len(dictionary[self.word])):
                answer += f'{str(i+1)}. {dictionary[self.word][i]}'
                answer += '\n'

        # Print correct answer
        if input in list(dictionary[self.word]) or input == dictionary[self.word]:
            self.ids[f'correct{str(self.id+1)}'].text = 'CORRECT'
            self.ids[f'correct{str(self.id+1)}'].color = (0, 1, 0, 1)
            self.ids[f'answer{str(self.id+1)}'].text = answer
            correct_counter += 1
            self.ids[f'score{str(self.id+1)}'].text = str(correct_counter)
        else:
            self.ids[f'correct{str(self.id+1)}'].text = 'INCORRECT'
            self.ids[f'correct{str(self.id+1)}'].color = (1, 0, 0, 1)
            self.ids[f'answer{str(self.id+1)}'].text = answer

        self.ids[f'next{str(self.id+1)}'].disabled = False
        self.ids[f'check{str(self.id+1)}'].disabled = True

    def pass_score(self):
        try:
            self.manager.get_screen(f'card{str(self.id+2)}').ids[f'score{str(self.id+2)}'].text \
            = self.manager.get_screen(f'card{str(self.id+1)}').ids[f'score{str(self.id+1)}'].text
        except:
            total = self.manager.get_screen(f'card{str(self.id+1)}').ids[f'score{str(self.id+1)}'].text
            self.manager.get_screen('result').ids['result_value'].text = f'{total} / 20'
#
# UWAGA! We wszystkich funkcjach ze zmiennymi po self.id należy dodać warunki brzegowe
# Możliwe błędy przy ostatniej karcie

class Card1(Card):
    id = 0

class Card2(Card):
    id = 1

class Card3(Card):
    id = 2

class Card4(Card):
    id = 3

class Card5(Card):
    id = 4

class Card6(Card):
    id = 5

class Card7(Card):
    id = 6

class Card8(Card):
    id = 7

class Card9(Card):
    id = 8

class Card10(Card):
    id = 9

class Card11(Card):
    id = 10

class Card12(Card):
    id = 11

class Card13(Card):
    id = 12

class Card14(Card):
    id = 13

class Card15(Card):
    id = 14

class Card16(Card):
    id = 15

class Card17(Card):
    id = 16

class Card18(Card):
    id = 17

class Card19(Card):
    id = 18

class Card20(Card):
    id = 19

class Result(Card):
    pass


gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        Window.size = (400, 600)
        return gui

if __name__ == '__main__':
    EnglishApp().run()
