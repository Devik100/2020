try:
    x = input('''What message do you wish to spam with? ''')
    output = '''
Copy the below text:
'''
    y = int(input('How many lines of spam? '))

    z = 0

    while z <= y:
        output += x
        output += '''
'''

        z += 1
    output += f'''That's {y} lines of spam up there. Use Shift + Up_Arrow from here after highlighting the last \'{x[-1]}\' in {x}'''
    print(output)

except ValueError:
    print('Please enter a value.')

except IndexError:
    print('Please enter a value.')
# Now run this in a Python 3 program app and enter the values.

