from random import randint
import funcs_logic
import funcs_interface
from classes import WindowMaker, CheckButton, AnswerButton

replay = []
while not replay:
    game_rules = "Rules:\nThere is a field with numbers on the left, right, top and bottom. Your task is\nto color " \
                 "all boxes using 2 colors: black and yellow. Numbers on the left and\ntop show the maximum amount of " \
                 "black boxes that should be present in\na row or column. Yellow boxes - numbers on the right " \
                 " and bottom.To color box black tap on the box once, to color yellow - twice. \nFill all boxes. Press " \
                 "the 'Check' button after you finish.\nThe game can be only closed in messagebox that appears after " \
                 "you press\n'Check!'.Good luck : ) "
    game_name = "Lerogram"
    bg_color = '#0049b8'
    main_window = WindowMaker(game_name, game_rules, bg_color, replay)
    # make label bg and rules sections
    funcs_interface.make_window_label_board(main_window)
    # make black and yellow boxes in the corners
    funcs_interface.make_two_color_boxes()
    # create an array for all pressed buttons and their color
    all_coords = []
    # generate yellow dots in amount of random range
    yel_dots = funcs_logic.generate_yel_dots(randint(100, 200))
    # solution
    funcs_logic.print_answer(yel_dots)
    # depending on the placement of yellow dots count maximum amounts for boxes
    bl_horiz, yel_horiz = funcs_logic.find_max_hor(yel_dots)
    bl_vert, yel_vert = funcs_logic.find_max_vert(yel_dots)
    # create vertical and horizontal lines of numbers
    funcs_interface.make_num_horiz_board(bl_horiz, yel_horiz)
    funcs_interface.make_num_vert_board(bl_vert, yel_vert)
    # create field with buttons
    funcs_interface.create_button_field(all_coords)
    # work with an array all_coords
    # button to check user input
    CheckButton(all_coords, bl_horiz, yel_horiz, bl_vert, yel_vert, main_window)
    # button to show right answer
    AnswerButton(yel_dots)
    # if the answer is correct right_answer window will appear
    # otherwise fail_window
    main_window.mainloop()
