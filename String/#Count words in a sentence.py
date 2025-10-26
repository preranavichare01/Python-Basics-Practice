#Count words in a sentence
text="This is my world!!"
clean_text=""
for char in text:
    if char.isalpha() or char==" ":
        clean_text+=char

my_word=[]
count=0
my_word=clean_text.split()
for word in my_word:
    count+=1
print(count)

