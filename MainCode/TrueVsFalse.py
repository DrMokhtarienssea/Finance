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

buildkv = Builder.load_file("truevsfalsefinance.kv")

class TrueorFalse(App):
    def build(self):
        return buildkv

points = 0 ##global variable
if __name__ == '__main__':
    TrueorFalse().run()