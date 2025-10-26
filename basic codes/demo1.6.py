#Generate Fibonacci series

a=0
b=1
n=5 # generate for 5th so ans should be 3

for i in range (0,n-2):
    c=a+b
    a=b
    b=c

print(c)

