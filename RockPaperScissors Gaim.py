Round = 1
import random

GaimChamps = ['Alex', 'Bob', 'Carl', 'David', 'Eric', 'Felix', 'George', 'Harold', 'Isabelle', 'John', 'Kyle', 'Liam', 'Mary', 'Nancy', 'Olivia', 'Peter', 'Quincy', 'Robert', 'Sam', 'Tim', 'Uda', 'Victor', 'William', 'Xavier', 'Yousef', 'Zoe'] #These names totally aren't alphebetical
Human = input('''Welcome to Rock Paper Scissors Gaim!
We will automatically pair you up with some Gaim champions.
To do that, we need to know your name: ''')
Computer = GaimChamps[random.randint(0, 25)]

def rps(Round):
    output = ''
    playerInput = input(f"""Rock Paper Scissors Gaim - Round {Round}! {Human} -VS- {Computer}!

    Do you use:
Rock
Paper
or Scissors? """).lower()
    print(f'''Waiting for {Computer} to make his move...
Outputting answers...
''')
    computerInput = random.randint(1, 3)
    if computerInput == 1:
        if playerInput == 'rock':
            output = f'{Computer} and {Human} both picked rock!'
        elif playerInput == 'paper':
            output = f'{Human} (Paper) beat {Computer} (Rock)!'
        elif playerInput == 'scissors':
            output = f'{Computer} (Rock) beat {Human} (Scissors)!'
        else:
            output = f'Human was disqualified from Round {Round} due to entering an invalid text!'
    elif computerInput == 2:
        if playerInput == 'rock':
            output = f'{Computer} (Paper) beat {Human} (Rock)!'
        elif playerInput == 'paper':
            output = f'{Computer} and {Human} both picked paper!'
        elif playerInput == 'scissors':
            output = f'{Human} (Scissors) beat {Computer} (Paper)!'
        else:
            output = f'{Human} was disqualified from Round {Round} due to entering an invalid text!'
    else:
        if playerInput == 'rock':
            output = f'{Computer} (Paper) beat {Human} (Rock)!'
        elif playerInput == 'paper':
            output = f'{Computer} (Scissors) beat {Human} (Paper)!'
        elif playerInput == 'scissors':
            output = f'{Computer} and {Human} both picked scissors!'
        else:
            output = f'{Human} was disqualified from Round {Round} due to entering an invalid text!'
    print(f'Result of Round {Round} - {Human} -VS- {Computer}: {output}')
    shallRepeat = input('Do you want a rematch? Yes/No ').lower()
    if shallRepeat == 'yes':
        print()
        rps(Round + 1)
    elif shallRepeat == 'No':
        print('Ok, then.')
    else:
        print("... I'm assuming you do... not.")


rps(Round)
