from tkinter import *
import tkinter as tk
import funcs_buttons
import funcs_interface


class WindowMaker(Tk):
    def __init__(self, game_name=" ", bg_color=" ", replay=[]):
        super().__init__()
        self.game_title = game_name
        self.bg_color = bg_color
        self.replay = replay

    def make_the_window(self):
        # configure the root window
        self.title(self.game_title)
        self.geometry('700x700')
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
        self.bind('<Button-1>',
                  lambda event, but=self, i=i, j=j: funcs_buttons.pressed_once(event, but, i, j, all_coords))
        self.bind('<Double-1>',
                  lambda event, but=self, i=i, j=j: funcs_buttons.pressed_twice(event, but, i, j, all_coords))


class CheckButton(Button):
    def __init__(self, all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz, window):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Check!"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: funcs_buttons.check_us_input(all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz,
                                                               window)
        self.place(x=210, y=530)


class SolveButton(Button):
    def __init__(self, all_coords, right_coords, window):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Solve"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: funcs_interface.create_right_button_field(all_coords, right_coords, window)
        self.place(x=410, y=530)


class AnswerButton(Button):
    def __init__(self, yel_coord):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Answer"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: funcs_buttons.show_answer(yel_coord)
        self.place(x=310, y=530)


class ExitButton(Button):
    def __init__(self, window):
        Button.__init__(self)
        self['bg'] = 'red'
        self['text'] = "X"
        self['width'] = 5
        self['height'] = 2
        self['command'] = lambda: funcs_buttons.exit_message(window)
        self.place(x=610, y=20)


class RulesButton(Button):
    def __init__(self, game_rules, bg_color):
        self.bg_color=bg_color
        self.game_rules = game_rules
        Button.__init__(self)
        self['bg'] = 'yellow'
        self['text'] = "Rules"
        self['width'] = 5
        self['height'] = 2
        self['command'] = lambda: RulesButton.make_new_window(self)
        self.place(x=50, y=20)

    def make_rules(self, new_window):
        rules = tk.Text(new_window, bg='#eaf205', bd=1, font=('Calibri Light', 14, 'bold'), padx=10, width=60, height=9)
        rules.insert(INSERT, self.game_rules)
        rules.place(x=10, y=100)

    def make_new_window(self):
        new_window = WindowMaker("Rules", self.bg_color)
        new_window.make_the_window()
        RulesButton.make_rules(self, new_window)
        ExitButton(new_window)


