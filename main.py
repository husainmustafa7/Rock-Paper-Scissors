import random

def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie'
    
    if won(user, computer):
        return 'you Won!'
    
    return 'You Lost!'
    
def won(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')  or (player == 'p' and opponent == 'r'):
        return True
    
print(play())