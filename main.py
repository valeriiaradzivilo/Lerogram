from random import randint
import funcs_logic
import funcs_interface
from classes import WindowMaker, CheckButton, AnswerButton, SolveButton, ExitButton, RulesButton

replay = []
while not replay:
    game_rules = "Rules:\n\nLerogram is a logic game on a field of 15x15 cells for one player.\nThere are numbers on " \
                 "the left, right, bottom, and top.\nThe numbers on the left and top indicate which the longest block " \
                 "of black cells is present in this row or column.\nSimilarly, the numbers on the right and bottom " \
                 "indicate which the longest block of yellow cells is present in a given column or row.\nThere may be " \
                 "several such blocks, but the length of none of them should not exceed the maximum value.\nThere " \
                 "must also be a block equal in length to this value.\n\nIf the player does not exceed the maximum " \
                 "length in all blocks – he wins,\nif not – loses. To check the correctness of the input,you need to " \
                 "click Check.\nAnd to get a hint – Answer.\nIf the task is too difficult, the computer can solve it " \
                 "for you.\nTo do this, simply press the Solve button.\nTo close the game, you need to click on the " \
                 "red button with a cross\nnext to the title.If you try to exit the game in the usual way -\nthe game " \
                 "will reboot.\nGood luck : ) \n\n     About:\nMade by Radzivilo Valeriia IP-14 2022 "
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
