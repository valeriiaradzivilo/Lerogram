from random import randint


def right_answer(yel_dots):
    answer = yel_dots.copy()
    for i in range(15):
        for j in range(15):
            if (i, j, 'y') not in yel_dots and j != 15:
                answer.append((i, j, "b"))
    answer.sort()
    return answer


def generate_yel_dots(amount):
    yel_dots = []
    for s in range(amount):
        i = randint(0, 14)
        j = randint(0, 14)
        yel_dots.append((i, j, 'y'))

    for i in range(15):
        yel_dots.append((i, 15, 'y'))
        yel_dots.append((15, i, 'y'))
    yel_dots = list(set(yel_dots))
    yel_dots.sort()
    return yel_dots


def print_answer(yel_dots):
    print("Answer(yellow dots): ")
    for i in range(15):
        row = []
        for j in range(15):
            if (i, j, 'y') in yel_dots and j != 15:
                row.append(j + 1)
            if j == 14:
                print(i + 1, " : ", row)


def find_max_hor(yel_dots):
    # Black verticals
    amounts_bl_vert = []
    for i in range(15):
        result = 0
        max_bl = 0
        for j in range(15):
            if (i, j, 'y') not in yel_dots:
                max_bl += 1
                if (i, j + 1, 'y') in yel_dots:
                    if max_bl >= result:
                        result = max_bl
                    max_bl = 0
        amounts_bl_vert.append(result)

    # Yellow verticals
    amounts_yel_ver = []

    for i in range(15):
        max_yel = 0
        result_yel = 0
        for j in range(15):
            if (i, j, 'y') in yel_dots:
                max_yel += 1
                if (i, j + 1, 'y') not in yel_dots or j + 1 == 15:
                    if max_yel >= result_yel:
                        result_yel = max_yel
                    max_yel = 0
        amounts_yel_ver.append(result_yel)

    return amounts_bl_vert, amounts_yel_ver


def find_max_vert(yel_dots):
    # Black horizontals
    amounts_bl_horiz = []
    for j in range(15):
        result = 0
        max_bl = 0
        for i in range(15):
            if (i, j, 'y') not in yel_dots:
                max_bl += 1
                if (i + 1, j, 'y') in yel_dots:
                    if max_bl >= result:
                        result = max_bl
                    max_bl = 0
        amounts_bl_horiz.append(result)

    # Yellow verticals
    amounts_yel_horiz = []

    for j in range(15):
        max_yel = 0
        result_yel = 0
        for i in range(15):
            if (i, j, 'y') in yel_dots:
                max_yel += 1
                if (i + 1, j, 'y') not in yel_dots or i + 1 == 15:
                    if max_yel >= result_yel:
                        result_yel = max_yel
                    max_yel = 0
        amounts_yel_horiz.append(result_yel)

    return amounts_bl_horiz, amounts_yel_horiz


def take_yels(all_coords):
    yel_dots = []
    for i in range(15):
        for j in range(15):
            if (i, j, 'y') in all_coords:
                yel_dots.append((i, j, 'y'))
    return yel_dots
