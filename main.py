import funcs_logic
import funcs_interface
from classes import WindowMaker, CheckButton

game_rules = "The rules:\nThere is a field with numbers on the left, right, top and bottom.\nYour task is to color " \
             "all boxes using 2 colors: black and yellow.\nNumbers on the left and top show the maximum amount of " \
             "black boxes in a row\nor column. Numbers on the right and bottom are maximum for yellow boxes.\nTo " \
             "color box black tap on the box once, to color yellow - twice.\nPress the button 'Check' after you " \
             "finish. "
game_name = "Lerogram"
bg_color = '#4C00C9'
main_window = WindowMaker(game_name, game_rules, bg_color)
# make label bg and rules sections
funcs_interface.make_window_label_board(main_window)
# make black and yellow boxes in the corners
funcs_interface.make_two_color_boxes()
# create an array for all pressed buttons and their color
all_coords = []
yel_dots = funcs_logic.generate_yel_dots(100)
print("Answer:", yel_dots)
bl_horiz, yel_horiz = funcs_logic.find_max_hor(yel_dots)
bl_vert, yel_vert = funcs_logic.find_max_vert(yel_dots)

funcs_interface.make_num_horiz_board(bl_horiz, yel_horiz)
funcs_interface.make_num_vert_board(bl_vert, yel_vert)

funcs_interface.create_button_field(all_coords)

# work with an array all_coords
CheckButton(all_coords, bl_horiz, yel_horiz, bl_vert, yel_vert)

main_window.mainloop()
