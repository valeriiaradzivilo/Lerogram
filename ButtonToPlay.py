from tkinter import Button
import funcs_buttons


class ButtonToPlay(Button):
    def __init__(self, i = 0, j = 0, all_coords = []):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = " "
        self['width'] = 2
        self['height'] = 1
        self.bind('<Button-1>',
                  lambda event, but=self, i=i, j=j: ButtonToPlay.pressed_once(event, but, i, j, all_coords))
        self.bind('<Double-1>',
                  lambda event, but=self, i=i, j=j: ButtonToPlay.pressed_twice(event, but, i, j, all_coords))

    def pressed_once(event, but, i, j, all_coords):
        but["bg"] = "black"
        all_coords.append((i, j, "b"))
        while (i, j, "y") in all_coords:
            all_coords.remove((i, j, "y"))

    def pressed_twice(event, but, i, j, all_coords):
        but["bg"] = "yellow"
        all_coords.append((i, j, "y"))
        while (i, j, "b") in all_coords:
            all_coords.remove((i, j, "b"))
