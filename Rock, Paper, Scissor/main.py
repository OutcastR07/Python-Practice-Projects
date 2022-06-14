import random

def play():
    user = input("What's your choise? 'p' for paper, 'r' for rock, 's' for scissor\n")
    computer = random.choice(['r', 's', 'p'])

    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

    if user == computer:
        return "It's a TIE!!"

    if is_win(user, computer):
        return "You WIN!!!"

    return "You LOSE!"

print(play())
