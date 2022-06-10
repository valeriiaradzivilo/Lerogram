from tkinter import Button
import funcs_buttons


class CheckButton(Button):
    def __init__(self, all_coords=[], bl_vert=[], yel_vert=[], bl_horiz=[], yel_horiz=[], window=None):
        Button.__init__(self)
        self['bg'] = 'white'
        self['text'] = "Check!"
        self['width'] = 10
        self['height'] = 2
        # function that will check user input after user presses the button
        self['command'] = lambda: funcs_buttons.check_us_input(all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz,
                                                               window)
        self.place(x=210, y=530)
