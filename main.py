from random import randint
import funcs_logic
import funcs_interface
from classes import WindowMaker, CheckButton, AnswerButton, SolveButton, ExitButton, RulesButton

replay = []
while not replay:
    game_rules = "Rules:\n\nThere is a field with numbers on the left, right, top and bottom. \nYour task is to color " \
                 "all boxes using 2 colors: black and yellow.\nNumbers on the left and top show the maximum length of " \
                 "black boxes\nback-to-back that should be present in a row or column.\nYellow boxes - numbers on the right " \
                 " and bottom.\nTo color box in black tap on the box once, to color yellow - twice. \nFill all boxes. Press " \
                 "the 'Check' button after you finish.\nThe game can be only closed in messagebox that appears after " \
                 "you press\n'Check!' or using button 'X' right next to the game's title.\nIf you press ordinary window exit button - the game will restart!\nGood luck : ) \n\n     About:\nMade by Radzivilo Valeriia IP-14 2022 "
    game_name = "Lerogram"
    bg_color = '#0049b8'
    main_window = WindowMaker(game_name, bg_color, replay)
    # make label bg and rules sections
    funcs_interface.make_window_label_board(main_window)
    # make black and yellow boxes in the corners
    funcs_interface.make_two_color_boxes()
    # create an array for all pressed buttons and their color
    all_coords = []
    # generate yellow dots in amount of random range
    yel_dots = funcs_logic.generate_yel_dots(randint(100, 200))
    # solution
    # funcs_logic.print_answer(yel_dots)
    # depending on the placement of yellow dots count maximum amounts for boxes
    bl_horiz, yel_horiz = funcs_logic.find_max_hor(yel_dots)
    bl_vert, yel_vert = funcs_logic.find_max_vert(yel_dots)
    # create vertical and horizontal lines of numbers
    funcs_interface.make_num_horiz_board(bl_horiz, yel_horiz)
    funcs_interface.make_num_vert_board(bl_vert, yel_vert)
    # create field with buttons
    funcs_interface.create_button_field(all_coords)
    # work with an array all_coords
    # create the right answer
    right_answer = funcs_logic.right_answer(yel_dots)
    # button to solve task
    SolveButton(all_coords, right_answer,main_window)
    # button to check user input
    CheckButton(all_coords, bl_horiz, yel_horiz, bl_vert, yel_vert, main_window)
    # button to show right answer
    AnswerButton(yel_dots)
    # if the answer is correct right_answer window will appear
    # otherwise fail_window
    # button to quit game
    ExitButton(main_window)
    RulesButton(game_rules, bg_color)
    main_window.mainloop()
