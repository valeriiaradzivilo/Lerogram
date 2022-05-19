from tkinter import *
import tkinter as tk
import funcs


class WindowMaker(Tk):
    def __init__(self, game_name=" ", game_rules=" ", bg_color=" ", replay=[]):
        super().__init__()
        self.game_rules = game_rules
        self.game_title = game_name
        self.bg_color = bg_color
        self.replay = replay

    def make_the_window(self):
        # configure the root window
        self.title(self.game_title)
        self.geometry('700x750')
        # forbid to change window size
        self.resizable(0, 0)
        self.config(bg=self.bg_color)

    def make_label(self):
        # text "Lerogram" on top of the game
        tk.Label(
            text=self.game_title,
            foreground="white",
            bg=self.bg_color,
            font=("Calibri Light", 48)
        ).place(
            relx=0.5,
            rely=0.05,
            anchor='center'
        )

    def make_rules(self):
        rules = tk.Text(self, bg='white', bd=1, font=('Calibri Light', 14, 'bold'))
        rules.insert(INSERT, self.game_rules)
        rules.place(
            relx=0.01,
            rely=0.77
        )


class ColorAmounts(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['bg'] = 'white'
        self['width'] = 2
        self['height'] = 1


class ButtonToPlay(Button):
    def __init__(self, i, j, all_coords):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = " "
        self['width'] = 2
        self['height'] = 1
        self.bind('<Button-1>', lambda event, but=self, i=i, j=j: funcs.pressed_once(event, but, i, j, all_coords))
        self.bind('<Double-1>', lambda event, but=self, i=i, j=j: funcs.pressed_twice(event, but, i, j, all_coords))


class CheckButton(Button):
    def __init__(self, all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz, window):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Check!"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: funcs.check_us_input(all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz, window)
        self.place(x=310, y=530)

