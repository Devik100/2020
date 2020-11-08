Round = 1
import random

print('Welcome to:')


def rps(Round):
    output = ''
    playerInput = input(f"""Minecraft - Rock Paper Scissors - Tool Block Mob! - Round {Round}! Human -VS- Computer!

    Do you use:
Tool
Block
or Mob?
Tool beats block, block beaTs mob, aNd mob beaTs tool """).lower()
    print('''Calculating...
Using logic functions...
Spawning enDermen...
PlantIng seeds...
Deafeating raids...
ExploRing basTions...
Mining coal...
Blowing up chourus fruit...
Building iron golems...
Generating World...
Outputting answers...
''')
    computerInput = random.randint(1, 3)

    if computerInput == 1:
        if playerInput == 'tool':
            output = 'Tie!'
        elif playerInput == 'block':
            output = 'Human wins!'
        elif playerInput == 'mob':
            output = 'Computer wins!'
        else:
            output = f'Human was disqualified from Round {Round} due to entering an invalid text!'
    elif computerInput == 2:
        if playerInput == 'tool':
            output = 'Computer wins!'
        elif playerInput == 'block':
            output = 'Tie!'
        elif playerInput == 'mob':
            output = 'Human wins!'
        else:
            output = f'Human was disqualified from Round {Round} due to entering an invalid text!'
    else:
        if playerInput == 'tool':
            output = 'Computer wins!'
        elif playerInput == 'block':
            output = 'Human wins!'
        elif playerInput == 'mob':
            output = 'Tie!'
        else:
            output = f'Human was disqualified from Round {Round} due to entering an invalid text!'
    if playerInput == 'dirt':
        output = 'Human was trampled by Computer!'
    if playerInput == 'tnt':
        output = 'Computer was blown up by Human!'

    print(f'Reslult of Round {Round} - Human -VS- Computer: {output}')
    shallRepeat = input('Do you want a rematch? Yes/No ').lower()
    if shallRepeat == 'yes':
        print()
        rps(Round + 1)
    elif shallRepeat == 'No':
        print('Ok, then.')
    else:
        print("... I'm assuming you do... not.")


rps(Round)
