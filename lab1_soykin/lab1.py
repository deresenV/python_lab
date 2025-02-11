def check_pos(x, y, danger_zones):
    min_coords, max_coords = 1, 100
    if x > max_coords or x < min_coords or y > max_coords or y < min_coords:
        print("Дальше проход невозможен!\nКонец карты!")
        return False
    if [x, y] in danger_zones:
        print("Дальше проход невозможен!\nЗапретная зона!")
        return False
    return True
def move(rotation, steps, x, y, log_moves, danger_zones, logger=True):
    move_count=0
    for _ in range(steps):
        new_x, new_y = x, y
        if rotation == 'R':
            new_x += 1
        elif rotation == 'L':
            new_x -= 1
        elif rotation == 'U':
            new_y -= 1
        elif rotation == 'D':
            new_y += 1

        if check_pos(new_x, new_y, danger_zones):
            x, y = new_x, new_y
            move_count += 1
            print(x, y)
        else:
            break
    if logger:
        log_moves.insert(0, (rotation, move_count))


    return x, y, log_moves

def reverse_rotation(rotation):
    if rotation == 'R':
        return "L"
    if rotation == 'L':
        return "R"
    if rotation == 'U':
        return "D"
    if rotation == 'D':
        return "U"

def back(log_moves, x, y, danger_zones, steps_back=1):
    if not log_moves:
        print("Использование B недоступно! Нет записанных ходов.")
        return x, y, log_moves

    steps_back = min(steps_back, len(log_moves))

    for _ in range(steps_back):
        last_move = log_moves.pop(0)
        rotation, steps = last_move
        x, y, log_moves = move(reverse_rotation(rotation), steps, x, y, log_moves, danger_zones, False)

    return x, y, log_moves

def zones(command):
    x,y,w,h = map(int,command)
    danger_zones = []
    for j in range(y,h+y):
        for i in range(x,x+w):
            danger_zones.append([i,j])
    return danger_zones


def main_game():
    x, y = 1, 1
    log_moves = []
    danger_zones = []
    commands=[]
    while True:
        input_command=input().split(',')
        if input_command[0]=='do':
            for command in commands:
                if command[0] == 'B':
                    steps_back = int(command[1]) if len(command) > 1 else 1
                    x, y, log_moves = back(log_moves, x, y, danger_zones, steps_back)

                elif len(command) == 2:
                    rotation, steps = command[0], int(command[1])
                    x, y, log_moves = move(rotation, steps, x, y, log_moves, danger_zones)

                elif len(command) == 4:
                    danger_zones = zones(command)

                else:
                    print("Некорректная команда!")
            commands=[]
        else:
            commands.append(input_command)



main_game()
