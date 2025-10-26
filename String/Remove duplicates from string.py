# Remove duplicates from strING
text="prerana"
my_list=[]
for char in text:
    if char in my_list:
        pass
    else:
        my_list.append(char)

res=''.join(my_list)
print(res)