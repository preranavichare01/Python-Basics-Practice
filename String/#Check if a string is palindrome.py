#Check if a string is palindrome
word=input("enter string").lower()
temp=word
if word[::-1]==temp:
    print("palindrome")
else:
    print("not palindrome")