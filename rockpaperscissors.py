#! python3
# rockpaperscissors.py: traditional game of Rock-Paper-Scissors
#                       played against computer. Keeps track of 
#                       score per game.

import random, sys

print('ROCK-PAPER-SCISSORS')

# These variables will keep track of the wins, losses and ties.
wins = 0
losses = 0
ties = 0

# Main Game Loop
while True:
    print('%s Wins, %s Losses, %s Ties\n'%(wins, losses, ties))

    # Main User Input Loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()

        if playerMove == 'q':
            sys.exit()          # QUIT PROGRAM

        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break               # break out of user input loop

        print('Type one of r, p, s, or q.')     # re-prompt user for apporopriate input

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display computer's move
    randomNum = random.randint(1,3)
    if randomNum == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNum == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNum == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1