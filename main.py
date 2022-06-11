import regular_game

# array to record replays
replay = ['y']
# array to record created task
create = []
# create an array for all presssed buttons and their color
all_coords = []
# level
amounts = []
# while user wants to replay
re = 0
while True:
    regular_game.regular_game(create, replay, all_coords, amounts)
    if replay and replay.pop() == 'n':
        break
    print("Replay in main: ", replay)
