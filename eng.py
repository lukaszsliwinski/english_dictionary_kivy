from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.core.window import Window

import csv
import random


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



num_of_words = 3


# Choose random polish words to translate and save to list
def choose_words(dictionary):
    pl_words = []
    i = 0
    while i < num_of_words:
        random_word = random.choice(list(dictionary))
        if random_word not in pl_words:
            pl_words.append(random_word)
            i += 1
    return pl_words

# Create list with polish words to translate
pl_words = choose_words(dictionary)

class Start(Screen):
    pass


class Main(Screen):
    pl_words = choose_words(dictionary)

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.id = 0
        self.correct_counter = 0
        self.word = StringProperty()
        self.word = pl_words[self.id]
        self.word_label = f'{str(self.id+1)}. {self.word}'
        self.total = f' / {num_of_words}'
    
    # Check if answer is correct and print translation(s)
    def check(self):
        input = self.ids['input'].text
        self.ids['input'].readonly = True

        # Generate correct answer(s)
        answer = ''
        if len(dictionary[self.word]) == 1:
            answer = f'{dictionary[self.word][0]}'
        else:
            for i in range(len(dictionary[self.word])):
                answer += f'{str(i+1)}. {dictionary[self.word][i]}'
                answer += '\n'

        # Print correct answer(s)
        if input in list(dictionary[self.word]) or input == dictionary[self.word]:
            self.ids['correct'].text = 'CORRECT'
            self.ids['correct'].color = (0, 1, 0, 1)
            self.ids['answer'].text = answer
            self.correct_counter += 1
            self.ids['score'].text = str(self.correct_counter)
        else:
            self.ids['correct'].text = 'INCORRECT'
            self.ids['correct'].color = (1, 0, 0, 1)
            self.ids['answer'].text = answer

        # Change buttons states
        self.ids['next'].disabled = False
        self.ids['check'].disabled = True
        
        if self.id == num_of_words - 1:
            self.ids['result_btn'].disabled = False
            self.ids['result_btn'].opacity = 1
            self.ids['next'].disabled = True

    def next(self):
        self.id += 1
        self.word = pl_words[self.id]
        self.ids['word'].text = f'{str(self.id+1)}. {self.word}'
        self.ids['input'].readonly = False
        self.ids['input'].text = ''
        self.ids['correct'].text = ''
        self.ids['answer'].text = ''
        
        # Change buttons states
        self.ids['next'].disabled = True
        self.ids['check'].disabled = False

    def send_result(self):
        self.manager.get_screen('result').ids['result_value'].text = f'{self.correct_counter} / {num_of_words}'

class Result(Screen):
    pass


gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        Window.size = (400, 600)
        return gui

if __name__ == '__main__':
    EnglishApp().run()