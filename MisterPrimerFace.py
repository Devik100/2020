number = int(input('What number do you want to primeCheck? '))
is_prime = 1
if number > 0:
    for factor in range(2, number//2):
        if number % factor == 0:
            is_prime = 0
    number = str(number)
    if is_prime:
        print(number + ' is a prime!')
    else:
        print(number + ' is not prime!')