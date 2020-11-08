returnVar = 0
print("This is the calculator app.")


# The calculations must be in a function so that if a unidentified calculation is entered, we can repeat the process.
def calculate():
    operation = str(input('''What is the operation you wish to preform: Addition, Subtraction, Multiplication, Division, 
Power or Rounding? ''')).lower
    if operation == 'round':
        num1 = int(input('What is the number you want to round? '))

        print(f'Answer: {round(num1)}.')
    else:
        num1 = int(input('What is the first number? '))
        num2 = int(input('And the second? '))

        if operation == '''Add''':
            print('in the add statement')
            print(f'Answer: {num1 + num2}')

        elif operation == '''subtract''':
            print(f'Answer: {num1 - num2}')

        elif operation == '''multiply''':
            print(f'Answer: {num1 * num2}')

        elif operation == '''divide''':
            print(f'Answer: {num1 / num2}')

        elif operation == '''power''':
            print(f'Answer: {num1 ** num2}')
        else:
            print(f'''Invalid operation. Say:
Add
Subtract
Multiply
Divide
Power
Round
{operation}''')
            calculate()


calculate()