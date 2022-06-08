import regular_game
# array to record replays
replay = ['y']
# array to record created task
create = []
# create an array for all presssed buttons and their color
all_coords = []
# while user wants to replay
while replay and replay.pop() == 'y':
    regular_game.regular_game(create, replay, all_coords)
