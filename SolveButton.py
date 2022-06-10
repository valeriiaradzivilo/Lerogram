from ButtonToPlay import ButtonToPlay
import funcs_interface
from CheckButton import CheckButton


class SolveButton(CheckButton):
    def __init__(self, all_coords, right_coords, window):
        self.all_coords = all_coords
        self.right_coords = right_coords
        self.window = window
        super().__init__()
        self['text'] = "Solve"
        self['command'] = lambda: SolveButton.create_right_button_field(self)
        self.place(x=410, y=530)

    # create solution
    def create_right_button_field(self):
        self.all_coords.clear()
        for i in range(15):
            for j in range(15):
                b = ButtonToPlay(i, j, self.all_coords)
                b.place(x=165 + i * 24, y=115 + j * 25)
                if (i, j, 'b') in self.right_coords:
                    b.config(bg="black")
                    self.all_coords.append((i, j, 'b'))
                else:
                    b.config(bg="yellow")
                    self.all_coords.append((i, j, 'y'))
        # funcs_interface.result_message("You Won!", self.window)
