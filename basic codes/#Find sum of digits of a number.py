#Find sum of digits of a number

n=542
temp=0
while n>0:
    r=n%10
    temp=temp+r
    n=n//10
print(temp)