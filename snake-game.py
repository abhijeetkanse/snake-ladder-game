import random
import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGNETA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def r_dice() -> int:
    d = random.randint(1, 6)
    return d


player = [0, 0, 0, 0]
player_color = [GREEN, BLUE, RED, YELLOW]
col_name = ["Green", "Blue", "Red", "Yellow"]
player_name = []
colorama.init()
for i in range(4):
    player_name.append(input("{}For color {}, Enter your name : ".format(player_color[i], col_name[i])))
    print(RESET)

command = 'c'
dice = 0
snake = (21, 31, 44, 59, 74, 83, 95)
dest_snake = (8, 14, 26, 41, 49, 63, 25)

ladder = (7, 11, 23, 39, 46, 53, 61)
dest_ladder = (32, 29, 48, 54, 81, 77, 75)
flag = 0

while True:
    for i in range(4):
        if command == 'q' or command == 'Q':
            break
        elif command != 'c':
            command = input("Enter c to Continue OR q to Quit")

        if player[i] == 0 and command == 'c':
            dice = r_dice()
            print("{}Rolling Dice -- {}{}".format(player_color[i], dice, RESET))
            if dice == 6:
                player[i] = dice + player[i]
        elif player[i] <= 94 and command == 'c':
            dice = r_dice()
            print("{}Rolling Dice -- {}{}".format(player_color[i], dice, RESET))
            if dice + player[i] <= 100:
                player[i] = dice + player[i]
        elif player[i] <= 100:
            dice = r_dice()
            print("{}Rolling Dice -- {}".format(player_color[i], dice, RESET))
            if dice + player[i] <= 100:
                player[i] = dice + player[i]

        if player[i] in snake:
            temp = player[i]
            player[i] = dest_snake[snake.index(player[i])]
            msg = "AAAH.. Crap Snake got you at {}. You are at {} position".format(temp, player[i])
            OP_msg = "{}{}{}".format(player_color[i], msg, RESET)
            print(OP_msg)

        if player[i] in ladder:
            temp = player[i]
            player[i] = dest_ladder[ladder.index(player[i])]
            msg = "WOAH!! You got ladder at {}. You are at {} position".format(temp, player[i])
            OP_msg = "{}{}{}".format(player_color[i], msg, RESET)
            print(OP_msg)

        print("{}{} is at {} position{}".format(player_color[i], player_name[i], player[i], RESET))
        print("-" * 40)

        if player[i] == 100:
            print("{}{} is at {} position{}".format(player_color[i], player_name[i], player[i], RESET))
            print("*" * 40)
            text = "{}{} Has Won!! Congrats!!".format(player_color[i], player_name[i])
            print("**{0}{1}**".format(text.center(41), RESET))
            print("*" * 40)
            print()

            print("Final Positions :")
            for j in range(4):
                print("{}{} is at {}{}".format(player_color[j], player_name[j], player[j], RESET))
            flag = 1
            break

    if flag:
        break

colorama.deinit()
