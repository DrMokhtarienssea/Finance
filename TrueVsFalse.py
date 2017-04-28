# -*- coding: utf-8 -*-
"""
Application TrueVsFalse

@author: Max
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import time
import random

kv = '''
ScreenManagement:
    StartScreen:
    MainScreen:
    EndScreen:

<StartScreen>:
    name: "startScreen"
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source: 'main.jpg'
        GridLayout:
            padding: root.width * 0.4, root.height * .4
            spacing: "5dp"
            cols: 1
            Label:
                text: "True or False"
                bold: True
                font_size: "30dp"
            Button:
                text: "START"
                bold: True
                background_normal: "red.jpg"
                on_release: app.root.current = "mainScreen"
            Label:
                text: "Powered By Kivy"
                bold: True
                font_size: "14dp"

<MainScreen>:
    name: "mainScreen"
    on_enter: root.start()
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source: 'main.jpg'
        BoxLayout:
            size_hint:[1,.25]
            orientation: 'horizontal'
            GridLayout:
                cols: 1
                Label:
                    text: "Ques"
                    bold: True
                    font_size: '40dp'
                Label:
                    id: num
                    text: "1"
                    font_size: '30dp'
                    bold: True
            GridLayout:
                cols: 1
                Label:
                    text: "Points"
                    bold: True
                    font_size: '40dp'
                Label:
                    id: point
                    text: "0"
                    font_size: '30dp'
                    bold: True
        BoxLayout:
            size_hint:[1,.45]
            padding: root.width * 0.05, root.height * .05
            Label:
                id: question
                text: ""
                bold: True
                font_size: "20dp"
                text_size: (self.width, None)
        BoxLayout:
            size_hint:[1,.3]
            padding: root.width * 0.05, root.height * .05
            spacing: '5dp'
            Button:
                text: "True"
                bold: True
                background_normal: 'green.jpg'
                on_release: root.process(self.text)
            Button:
                text: "False"
                bold: True
                background_normal: 'red.jpg'
                on_release: root.process(self.text)

<EndScreen>:
    name: "endScreen"
    on_enter: root.refresh()
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source: 'main.jpg'
        GridLayout:
            padding: root.width * 0.4, root.height * .4
            spacing: "5dp"
            cols: 1
            Label:
                id: score
                text: ""
                bold: True
                font_size: "30dp"
            Button:
                text: "Play"
                bold: True
                background_normal: "red.jpg"
                on_release: app.root.current = "mainScreen"



'''
class StartScreen(Screen):
    pass
class MainScreen(Screen):
    question = ""
    answer = ""
    k = []
    done = []
    no = 0
    points = 0
    def start(self):
        self.question = ""
        self.answer = ""
        self.k = []
        self.done = []
        self.no = 0
        self.points = 0
        self.ids.point.text = str(0)
        self.ids.num.text = str(1)
        f = open('C:/Users/admin/OneDrive/Python/MindMap/data.txt', 'r')
        for i in f.readlines():
            j = []
            j.append(i.split(":")[0].strip("\n"))
            j.append(i.split(":")[1].strip("\n"))
            self.k.append(j)
        random.shuffle(self.k)
        r = random.randrange(1,len(self.k))
        self.question = self.k[r][0]
        self.answer = self.k[r][1]
        self.ids.question.text = self.question
        self.done.append(r)
        self.no += 1
    def process(self, text):
        if text == self.answer:
            self.points += 1
            self.ids.point.text = str(self.points)
        if self.no == 10:
            global points
            points = self.points
            self.manager.current = "endScreen"
        else:
            con = True
            while con:
                r = random.randrange(1,len(self.k))
                if r not in self.done:
                    self.question = self.k[r][0]
                    self.answer = self.k[r][1]
                    self.ids.question.text = self.question
                    self.done.append(r)
                    self.no += 1
                    self.ids.num.text = str(self.no)
                    con = False

class EndScreen(Screen):
    def refresh(self):
        global points
        self.ids.score.text = "You Score " + str(points)

class ScreenManagement(ScreenManager):
    points = 0

class TrueorFalse(App):
    def build(self):
        return Builder.load_string(kv)

points = 0 ##global variable
if __name__ == '__main__':
    TrueorFalse().run()