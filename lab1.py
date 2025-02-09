def check_pos(x,y, danger_zones):
    min_coords, max_coords = 1, 100
    if x>max_coords or y<min_coords or x<min_coords or y>max_coords:
        print("Дальше проход невозможен!\nКонец карты!")
        return False
    if [x, y] in danger_zones:
        print("Дальше проход невозможен!\nЗапретная зона!")
        return False
    return True
def move(rotation, steps, x, y, log_moves, danger_zones):
    log_moves.append((x,y))
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
            log_moves.append((x, y))
            print(x, y)
        else:
            break
    return x, y, log_moves

def back(log_moves):
    for i in log_moves[::-1][1:]:
        print(*i)
    return log_moves[0]

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
    danger_zones=[]
    while True:
        command = input().split()
        if len(command)==1:
            try:
                x, y = back(log_moves)
                log_moves = []
            except:
                print("Использование B недоступно!")
        elif len(command)==2:
            log_moves = []
            rotation, steps = command[0], int(command[1])
            x, y, log_moves = move(rotation, int(steps), x, y, log_moves, danger_zones)
        elif len(command)==4:
            danger_zones = zones(command)

main_game()