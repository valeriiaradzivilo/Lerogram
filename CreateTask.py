from tkinter import Button
from WindowMaker import WindowMaker
import funcs_interface
import regular_game

class CreateTask(Button):
    def __init__(self, old_window, bg_color, all_coord, create):
        self.old_window = old_window
        self.bg_color = bg_color
        self.all_coord = all_coord
        self.create = create
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Create Task"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: CreateTask.create_field(self)
        self.place(x=310, y=600)

    def create_field(self):
        self.all_coord.clear()
        self.old_window.destroy()
        new_window = WindowMaker("Create task", self.bg_color)
        new_window.make_the_window()
        funcs_interface.make_two_color_boxes()
        funcs_interface.create_button_field(self.all_coord)
        new_window.make_label()
        self.create.append('y')
        DoneTask(new_window, self.bg_color, self.all_coord, self.create)


class DoneTask(Button):
    def __init__(self, old_window, bg_color, all_coord, create):
        self.old_window = old_window
        self.bg_color = bg_color
        self.all_coord = all_coord
        self.create = create
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Done"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: CreateTask.create_field(self)
        self.place(x=310, y=600)

    def make_new_task(self):
        self.old_window.destroy()
        regular_game.regular_game(self.create, replay=[])
