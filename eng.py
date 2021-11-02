from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
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


class Start(Screen):
    question = f'How many words to choose? (max {len(dictionary.keys())}):'


class Main(Screen):
    id = 0
    correct_counter = 0
    pl_words = []


    def choose_words(self):
        self.num_of_words = int(self.manager.get_screen('start').ids['start_input'].text)
        i = 0
        while i < self.num_of_words:
            random_word = random.choice(list(dictionary))
            if random_word not in self.pl_words:
                self.pl_words.append(random_word)
                i += 1

        self.word = self.pl_words[self.id]
        self.ids['word'].text = f'{str(self.id+1)}. {self.word}'
        self.ids['total'].text = f' / {self.num_of_words}'


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
        self.ids['check'].disabled = True
        if self.id == self.num_of_words - 1:
            self.ids['result_btn'].disabled = False
            self.ids['result_btn'].opacity = 1
        else:
            self.ids['next'].disabled = False


    def next(self):
        self.id += 1
        self.word = self.pl_words[self.id]
        self.ids['word'].text = f'{str(self.id+1)}. {self.word}'
        self.ids['input'].readonly = False
        self.ids['input'].text = ''
        self.ids['correct'].text = ''
        self.ids['answer'].text = ''
        
        # Change buttons states
        self.ids['next'].disabled = True
        self.ids['check'].disabled = False


    def send_result(self):
        self.manager.get_screen('end').ids['result_value'].text = f'{self.correct_counter} / {self.num_of_words}'


class End(Screen):
    pass


gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        Window.size = (400, 600)
        return gui

if __name__ == '__main__':
    EnglishApp().run()