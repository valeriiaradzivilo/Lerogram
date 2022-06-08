import regular_game

replay = ['y']
create = []
# create an array for all presssed buttons and their color
all_coords = []
while replay and replay.pop() == 'y':
    regular_game.regular_game(create, replay, all_coords)
