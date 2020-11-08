try:
    print('''This is Guess Gaim!
    ''')
    import random

    GaimChamps = ['Alex', 'Bob', 'Carl', 'David', 'Eric', 'Felix', 'George', 'Harold', 'Isabelle', 'John', 'Kyle', 'Liam', 'Mary', 'Nancy', 'Olivia', 'Peter', 'Quincy', 'Robert', 'Sam', 'Tim', 'Uda', 'Victor', 'William', 'Xavier', 'Yousef', 'Zoe'] #These names totally aren't alphebetical

    Human = input('''Welcome to Guess Gaim!
    We will automatically pair you up with some Gaim Champions.
    To do that, we need to know your name: ''')

    Computer = GaimChamps[random.randint(0, 25)]

    count = 1

    print(f'{Computer} has chosen a number from 1 to 100! Try to guess it, {Human}!')

    number = random.randint(1, 100)

    guess = int(input(f'{Human}, guess {Computer}\'s number! Just enter your guess here: '))

    def guesss(guess):
        if guess != number:

            if guess > number:
                guess = int(input(f"{Human} guessed above {Computer}'s number! Try again: "))

            else:
                guess = int(input(f"{Human} guessed below {Computer}'s number! Try again: "))
            guesss(guess)
        else:
            print(f"{Human} wins!")

            if count > 50:
                print(f"It took {Human} {count} tries, but he still made it!")

            elif count > 10:
                print(f"{Human} took only {count} tries! Good job, {Human}!")

            else:
                print(f'Wow, {Human}! You took only {count} tries! You are as good as a Gaim Champion!')

    while guess != number:
        print(f'''This is Guess Gaim - round {count} - {Human} -VS- {Computer}''')
        guesss(guess)

        count += 1

except ValueError:
    print(f"""We cannot tolerate decimals, {Human}, for that is considered cheating! You have been disqualified,
and {Computer} has now won!""")