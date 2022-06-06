from tkinter import Button, INSERT
import tkinter as tk
from WindowMaker import WindowMaker


class RulesButton(Button):
    def __init__(self, game_rules, bg_color):
        self.bg_color = bg_color
        self.game_rules = game_rules
        Button.__init__(self)
        self['bg'] = 'yellow'
        self['text'] = "Rules"
        self['width'] = 5
        self['height'] = 2
        self['command'] = lambda: RulesButton.make_new_window(self)
        self.place(x=50, y=20)

    def make_rules(self, new_window):
        rules = tk.Text(new_window, bg='#eaf205', bd=1, font=('Calibri Light', 14, 'bold'), padx=10, pady=10, width=60,
                        height=25)
        rules.insert(INSERT, self.game_rules)
        rules.place(x=10, y=50)

    def make_new_window(self):
        new_window = WindowMaker("Rules", self.bg_color)
        new_window.make_the_window()
        RulesButton.make_rules(self, new_window)
