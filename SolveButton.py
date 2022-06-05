from tkinter import Button
from ButtonToPlay import ButtonToPlay
import funcs_interface


class SolveButton(Button):
    def __init__(self, all_coords, right_coords, window):
        self.all_coords = all_coords
        self.right_coords = right_coords
        self.window = window
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Solve"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: SolveButton.create_right_button_field(self)
        self.place(x=410, y=530)

    # create solution
    def create_right_button_field(self):
        for i in range(15):
            for j in range(15):
                b = ButtonToPlay(i, j, self.all_coords)
                b.place(x=165 + i * 24, y=115 + j * 25)
                if (i, j, 'b') in self.right_coords:
                    b.config(bg="black")
                else:
                    b.config(bg="yellow")
        funcs_interface.result_message("You Won!", self.window)
