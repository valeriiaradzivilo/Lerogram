from tkinter import Tk
import tkinter as tk


class WindowMaker(Tk):
    def __init__(self, game_name=" ", bg_color=" ", replay=[]):
        super().__init__()
        self.game_title = game_name
        self.bg_color = bg_color
        self.replay = replay

    # method to create the window
    def make_the_window(self):
        # configure the root window
        self.title(self.game_title)
        self.geometry('700x700')
        # forbid to change window size
        self.resizable(0, 0)
        self.config(bg=self.bg_color)

    # method to create title
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
