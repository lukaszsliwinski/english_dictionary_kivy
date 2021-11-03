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
    
    def check_and_choose(self):
        input_value = self.ids['start_input'].text
        try:
            input_value = int(input_value)
            if input_value > len(dictionary.keys()):
                self.ids['message_lbl'].text = f'There is only {len(dictionary.keys())} words in dictionary.'
            elif input_value <= 0:
                self.ids['message_lbl'].text = 'Minimum number is 1.'
            else:
                self.ids['start_btn'].disabled = False
                self.ids['start_btn'].opacity = 1
                self.ids['start_input'].readonly = True
                self.ids['choose_btn'].disabled = True
        except ValueError:
            if input_value == '':
                self.ids['message_lbl'].text = 'Enter the number of words.'
            else:
                self.ids['message_lbl'].text = 'It is not an integer number.'


class Main(Screen):
    id = 0
    correct_counter = 0
    pl_words = []


    def choose_words(self):
        self.num_of_words = int(self.manager.get_screen('start_screen').ids['start_input'].text)
        i = 0
        while i < self.num_of_words:
            random_word = random.choice(list(dictionary))
            if random_word not in self.pl_words:
                self.pl_words.append(random_word)
                i += 1

        self.word = self.pl_words[self.id]
        self.ids['word_lbl'].text = f'{str(self.id+1)}. {self.word}'
        self.ids['total_lbl'].text = f' / {self.num_of_words}'


    def check(self):
        input = self.ids['word_input'].text
        self.ids['word_input'].readonly = True

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
            self.ids['correct_lbl'].text = 'CORRECT'
            self.ids['correct_lbl'].color = (0, 1, 0, 1)
            self.ids['answer_lbl'].text = answer
            self.correct_counter += 1
            self.ids['score_lbl'].text = str(self.correct_counter)
        else:
            self.ids['correct_lbl'].text = 'INCORRECT'
            self.ids['correct_lbl'].color = (1, 0, 0, 1)
            self.ids['answer_lbl'].text = answer

        # Change buttons states
        self.ids['check_btn'].disabled = True
        if self.id == self.num_of_words - 1:
            self.ids['result_btn'].disabled = False
            self.ids['result_btn'].opacity = 1
        else:
            self.ids['next_btn'].disabled = False


    def next(self):
        self.id += 1
        self.word = self.pl_words[self.id]
        self.ids['word_lbl'].text = f'{str(self.id+1)}. {self.word}'
        self.ids['word_input'].readonly = False
        self.ids['word_input'].text = ''
        self.ids['correct_lbl'].text = ''
        self.ids['answer_lbl'].text = ''
        
        # Change buttons states
        self.ids['next_btn'].disabled = True
        self.ids['check_btn'].disabled = False


    def send_result(self):
        self.manager.get_screen('end_screen').ids['result_lbl'].text = f'{self.correct_counter} / {self.num_of_words}'


class End(Screen):
    pass


gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        Window.size = (400, 600)
        return gui

if __name__ == '__main__':
    EnglishApp().run()