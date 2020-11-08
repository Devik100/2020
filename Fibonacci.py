n = int(input('what is n? '))
a=0
b=1
sum=0
count=1
while(count < n+1):
    print(sum, end= ' ')
    count += 1
    a=b
    b=sum
    sum=a+b