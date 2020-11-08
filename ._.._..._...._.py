i = 1
w = input('What do you want to write with? ')
x = ''''''
z = int(input('How many lines do you want? '))
y = int(input('How fast do the lines grow? '))
output = ''''''
while i < z:
    i += 1
    x += w * y
    output += x
    output += '''
'''
print(output)