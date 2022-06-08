from tkinter import Button
from WindowMaker import WindowMaker
import funcs_interface
import regular_game


class CreateTask(Button):
    def __init__(self, old_window, bg_color, all_coord, create, main_window):
        self.old_window = old_window
        self.bg_color = bg_color
        self.all_coord = all_coord
        self.create = create
        self.main_window = main_window
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
        self.create.append(1)
        DoneTask(new_window, self.main_window, self.all_coord, self.create)


class DoneTask(Button):
    def __init__(self, old_window, main_window, all_coord, create):
        self.old_window = old_window
        self.main_window = main_window
        self.all_coord = all_coord
        self.create = create
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Done"
        self['width'] = 10
        self['height'] = 2
        self['command'] = lambda: DoneTask.make_new_task(self)
        self.place(x=310, y=600)

    def make_new_task(self):
        replay = ['y']
        # delete duplicates
        self.all_coord = list(set(self.all_coord))
        self.all_coord.sort()
        if len(self.all_coord) == 15 * 15:
            self.create.append(1)
            self.old_window.destroy()
            if not replay:
                print("no replay")
            regular_game.regular_game(self.create, replay, self.all_coord)

        else:
            if not replay:
                print("no replay")
            funcs_interface.wrong_create_message("You did not fill the field.", self.old_window)
            regular_game.regular_game(create=[0], all_coords=[], replay=replay)
