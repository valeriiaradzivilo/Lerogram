from tkinter import Label, messagebox

from classes import ColorAmounts, ButtonToPlay


def make_window_label_board(main_window):
    main_window.make_the_window()
    main_window.make_label()
    main_window.make_rules()


def make_two_color_boxes():
    # black box
    bl = Label(text=' ', bg='black', width=2, height=1)
    bl.place(x=140, y=90)

    # yellow box
    yel = Label(text=' ', bg='yellow', width=2, height=1)
    yel.place(x=530, y=493)


def make_num_vert_board(bl_vert, yel_vert):
    for i in range(15):
        bl_vert_num = ColorAmounts(text=bl_vert[i])
        bl_vert_num.place(x=140, y=117 + i * 25)

    for i in range(15):
        yel_vert_num = ColorAmounts(text=yel_vert[i])
        yel_vert_num.place(x=530, y=117 + i * 25)


def make_num_horiz_board(bl_horiz, yel_horiz):
    for i in range(15):
        bl_horiz_num = ColorAmounts(text=bl_horiz[i])
        bl_horiz_num.place(x=167 + i * 24, y=90)

    for i in range(15):
        yel_horiz_num = ColorAmounts(text=yel_horiz[i])
        yel_horiz_num.place(x=167 + i * 24, y=493)


def create_button_field(all_coords):
    for i in range(15):
        for j in range(15):
            ButtonToPlay(i, j, all_coords).place(x=165 + i * 24, y=115 + j * 25)


def result_message(mess, window):
    msgBox = messagebox.askquestion(mess, "Try again?")
    if msgBox == 'yes':
        print("Replaying the game")
        window.destroy()

    else:
        print("No replay")
        window.replay.append('n')
        window.destroy()
