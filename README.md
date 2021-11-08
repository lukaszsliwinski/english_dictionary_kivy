# English Dictionary (Kivy)

## About
Simply app to practice english vocabulary. Words with translates are saved in .csv file.<br><br>
Program algorythm:<br>
1 Import data from .csv and create dictionary<br>
2 Run app<br>
3 At first screen user determines how many random words wants to translate<br>
4 At second screen program displays first polish word<br>
5 User writes translation, checks if it's correct and goes to another word<br>
6 In the meantime program shows actual result<br>
7 After last word program shows final result at last screen and ends<br><br>
This app is an improved version of english app with tkinter GUI:<br>
https://github.com/lukaszsliwinski/english_dictionary

## Used technologies
Python 3.8<br>
Kivy 2.0

## Setup and run (Windows)
Instalation:<br>
1 Install Python 3.8 from website:<br>
&emsp;https://www.python.org/downloads/release/python-380/<br>
&emsp;Important - remember to mark "Add Python 3.8 to PATH"!<br>
&emsp;![alt text](https://github.com/lukaszsliwinski/english_dictionary_kivy/blob/master/add-python-to-path.png?raw=true)<br><br>
2 Download repository
```bash
git clone https://github.com/lukaszsliwinski/english_dictionary_kivy
```
3 Go into main directory
```bash
cd english_dictionary_kivy
```
4 Create virtual environment with Python 3.8 (you can use any name)
```bash
py -3.8 -m venv name
```
&emsp;This may take a while<br><br>
5 Run virtual environment
```bash
name\scripts\activate
```
&emsp;Important! Keep virtual environment running always when you use app. To deactivate venv use:
```bash
deactivate
```
6 With venv kept running install Kivy 2.0
```bash
python -m pip install kivy[full]
```
&emsp;This may take a while<br><br>
7 In main directory run eng.py file
```bash
python eng.py
```
<br>
To create your own database of words, you can edit dictionary.csv file