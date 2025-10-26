num = 392
temp = 0

while num > 0:
    r = num % 10      # get last digit
    temp = temp * 10 + r   # append digit
    num = num // 10   # remove last digit

print(temp)
