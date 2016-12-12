vector = [0, 0]


def determine_direction(turn, direction=[0]):
    turn_num = {'R': 1, 'L': -1}
    direction[0] = (direction[0] + turn_num[turn]) % 4

    return direction[0]

with open('day1.txt') as f:
    co_ordinates = [(x[0], int(x[1:])) for x in f.read().split(', ')]

    for p in co_ordinates:
        direction = determine_direction(p[0])

        if direction == 0:
            vector[1] += p[1]

        elif direction == 1:
            vector[0] += p[1]

        elif direction == 2:
            vector[1] -= p[1]

        else:
            vector[0] -= p[1]

print(sum(map(abs, vector)))
