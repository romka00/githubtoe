game =[
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
player_1 = input("Введите имя первого игрока, который будет играть за крестики:")
player_2 = input("Введите имя второго игрока, который будет играть за нолики:")

def game_area(game):
    game_c = game.copy()
    print(" \t0\t1\t2")
    c = 0
    for i in game_c:
        print(c, end="\t")
        c += 1
        for j in i:
            print(j, end="\t")
        print()


def check_win(game, x, y):
    if game[x][y] == game[x][y-1] == game[x][y-2]:
        return True
    if game[x][y] == game[x-1][y] == game[x-2][y]:
        return True
    if game[x][y] == game[0][0] == game[1][1] == game[2][2]:
        return True
    if game[x][y] == game[2][0] == game[1][1] == game[0][2]:
        return True

player = True
draw = 0
game_area(game)
while True:
    if draw < 9:

        if player:
            x, y = input(f"{player_1}, введите две координаты, через пробел:").split()
            game[int(x)][int(y)] = "X"
            game_area(game)
            if check_win(game, int(x), int(y)):
                print(f"{player_1}, победил!")
                break
            player = False
            draw += 1
        else:
            x, y = input(f"{player_2}, введите две координаты, через пробел:").split()
            game[int(x)][int(y)] = "0"
            game_area(game)
            if check_win(game, int(x), int(y)):
                print(f"{player_2}, победил!")
                break
            player = True
            draw += 1
    else:
        print("Ничья!")
        break