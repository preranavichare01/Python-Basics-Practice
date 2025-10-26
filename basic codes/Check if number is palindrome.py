#Check if number is palindrome

num=80
num=str(num)
temp=num

if num[::-1]==temp:
    print("palindrome")
else:
    print("not palindrome")