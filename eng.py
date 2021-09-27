from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

base_dict = {"kwestia" : ["issue", "matter"],
             "dowód" : ["evidence"],
             "prawie" : ["almost"],
            }

key_list = []

for i in base_dict.keys():
    key_list.append(i)




class Card(Screen):
    word = StringProperty()
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.test()
        self.word = key_list[self.id]

    def test(self):
        self.id = int()
       
    def check(self):
        answer = self.ids["input"+str(self.id+1)].text
        self.ids["input"+str(self.id+1)].readonly = True
        if answer in list(base_dict[key_list[self.id]]) or answer == base_dict[key_list[self.id]]:
            print("correct")
        else:
            print("incorrect")




class Card1(Card):
    def test(self):
        self.id = 0

class Card2(Card):
    def test(self):
        self.id = 1

class Card3(Card):
    def test(self):
        self.id = 2






gui = Builder.load_file('gui.kv')

class EnglishApp(App):
    def build(self):
        return gui

if __name__ == '__main__':
    EnglishApp().run()
