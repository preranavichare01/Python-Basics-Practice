text="prerana vichare"
text = text.replace(" ", "")
my_word={}
for char in text:
    if char in my_word:
        my_word[char]+=1
    else:
        my_word[char]=1


print(my_word)
