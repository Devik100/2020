def decide_number(n, k):
 num = 1
 if k > n - k:
    k = n - k
 for i in range(0, k):
    num = num * (n - i)
    num = num // (i + 1)
 return str(num)



rows = int(input('How many rows do you want? '))

m = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print(decide_number(i, j), end=' ')
    print(" ")