import funcs_interface


def pressed_once(event, but, i, j, all_coords):
    but["bg"] = "grey"
    all_coords.append((i, j, "b"))
    while (i, j, "y") in all_coords:
        all_coords.remove((i, j, "y"))


def pressed_twice(event, but, i, j, all_coords):
    but["bg"] = "yellow"
    all_coords.append((i, j, "y"))
    while (i, j, "b") in all_coords:
        all_coords.remove((i, j, "b"))


def check_us_input(all_coords, bl_vert, yel_vert, bl_horiz, yel_horiz):
    # delete duplicates
    all_coords = list(set(all_coords))
    # sort an array for easier use
    all_coords.sort()
    print("User input:", all_coords)
    check_if_right = []
    check_if_false = []
    # check if all boxes are colored
    check_all_colored(all_coords, check_if_right)
    check_verticals(all_coords, bl_vert, yel_vert, check_if_right)
    check_horizontals(all_coords, bl_horiz, yel_horiz, check_if_right)
    if not check_if_right:
        funcs_interface.right_answer()
    else:
        funcs_interface.error_message()


def check_all_colored(all_coords, check_if_right):
    user_coord_amount = len(all_coords)
    needed_coord_amount = 15 * 15
    # start all checks
    # if user doesn't fill the field
    if user_coord_amount != needed_coord_amount:
        print("in filling the field")
        check_if_right.append(1)


def check_verticals(all_coords, bl_vert, yel_vert, check_if_right):
    # Black verticals
    for j in range(15):
        list_of_lengths = []
        length = 0
        for i in range(15):
            if (j, i, 'b') in all_coords:
                length += 1
                if (j, i + 1, 'b') not in all_coords:
                    list_of_lengths.append(length)
                    i += 1
                    length = 0
        if not list_of_lengths:
            list_of_lengths.append(0)
        if bl_vert[j] not in list_of_lengths and all(x > bl_vert[j] for x in list_of_lengths):
            print("in black verticals")
            print(list_of_lengths)
            print("Supposed max: ", bl_vert[j])
            check_if_right.append(1)
    # Yellow verticals
    for j in range(15):
        list_of_lengths = []
        length = 0
        for i in range(15):
            if (j, i, 'y') in all_coords:
                length += 1
                if (j, i + 1, 'y') not in all_coords:
                    list_of_lengths.append(length)
                    i += 1
                    length = 0
        if not list_of_lengths:
            list_of_lengths.append(0)
        if yel_vert[j] not in list_of_lengths and all(x > yel_vert[j] for x in list_of_lengths):
            print("in yellow verticals")
            print(list_of_lengths)
            print("Supposed max: ", yel_vert[j])
            check_if_right.append(1)


def check_horizontals(all_coords, bl_horiz, yel_horiz, check_if_right):
    # Blacks horizontals
    for j in range(15):
        list_of_lengths = []
        length = 0
        for i in range(15):
            if (i, j, 'b') in all_coords:
                length += 1
                if (i + 1, j, 'b') not in all_coords:
                    list_of_lengths.append(length)
                    i += 1
                    length = 0
        if not list_of_lengths:
            list_of_lengths.append(0)
        if bl_horiz[j] not in list_of_lengths and all(x > bl_horiz[j] for x in list_of_lengths):
            print("in black horizontals")
            print(list_of_lengths)
            print("Supposed max: ", bl_horiz[j])
            check_if_right.append(1)

    # Yellow horizontals
    for j in range(15):
        list_of_lengths = []
        length = 0
        for i in range(15):
            if (i, j, 'y') in all_coords:
                length += 1
                if (i + 1, j, 'y') not in all_coords:
                    list_of_lengths.append(length)
                    i += 1
                    length = 0
        if not list_of_lengths:
            list_of_lengths.append(0)
        if yel_horiz[j] not in list_of_lengths and all(x > yel_horiz[j] for x in list_of_lengths):
            print("in yellow horizontals")
            print(list_of_lengths)
            print("Supposed max: ", yel_horiz[j])
            check_if_right.append(1)
