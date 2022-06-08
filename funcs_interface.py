from tkinter import Label, messagebox
from ColorAmounts import ColorAmounts
from ButtonToPlay import ButtonToPlay


# create the main window
def make_window_label_board(main_window):
    main_window.make_the_window()
    main_window.make_label()


# create 2 boxes in up-left corner and down-right
def make_two_color_boxes():
    # black box
    bl = Label(text=' ', bg='black', width=2, height=1)
    bl.place(x=140, y=90)

    # yellow box
    yel = Label(text=' ', bg='yellow', width=2, height=1)
    yel.place(x=530, y=493)


# create 2 vertical boards of numbers ( black and yellow )
def make_num_vert_board(bl_vert, yel_vert):
    for i in range(15):
        bl_vert_num = ColorAmounts(text=bl_vert[i])
        bl_vert_num.place(x=140, y=117 + i * 25)

    for i in range(15):
        yel_vert_num = ColorAmounts(text=yel_vert[i])
        yel_vert_num.place(x=530, y=117 + i * 25)


# create 2 horizontal boards of numbers ( black and yellow )
def make_num_horiz_board(bl_horiz, yel_horiz):
    for i in range(15):
        bl_horiz_num = ColorAmounts(text=bl_horiz[i])
        bl_horiz_num.place(x=167 + i * 24, y=90)

    for i in range(15):
        yel_horiz_num = ColorAmounts(text=yel_horiz[i])
        yel_horiz_num.place(x=167 + i * 24, y=493)


# create field 15 x 15 with buttons
def create_button_field(all_coords):
    for i in range(15):
        for j in range(15):
            ButtonToPlay(i, j, all_coords).place(x=165 + i * 24, y=115 + j * 25)


# messagebox that appears after user pressed on 'Check'
def result_message(mess, window):
    msgBox = messagebox.askquestion("Result", mess + " Try again?")
    if msgBox == 'yes':
        print("Replaying the game")
        window.replay.append('y')
        window.destroy()

    else:
        print("No replay")
        window.replay.append('n')
        window.destroy()


def wrong_create_message(mess, window):
    msgBox = messagebox.askquestion("Result", mess + " Try again?")
    if msgBox == 'yes':
        print("Turning back to main window")
        window.destroy()

    else:
        print("Turning back to main window")
        window.destroy()
