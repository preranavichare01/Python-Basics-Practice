#Find longest word in sentence
sen="This is my workplace."
sen=sen.replace(".", "").replace(",", "")
words=sen.split()
max_word=max(words,key=len)
print(max_word)
