"""my_list = input("Enter number separated by space:").split()
my_list = [int(num) for num in my_list]

max_number=max(my_list)
min_number=min(my_list)
print("max number:",max_number)
print("min number",min_number)

#anoter way
mylist = input("Enter numbers separated by space: ").split()
mylist = [int(num) for num in mylist]
mylist.sort()

print(mylist)
print("Max number:", mylist[-1])  # Last element after sort is max
print("Min number:", mylist[0])   # First element after sort is min

"""
nums = [567, 900, 12, 5, 80000]

max_num = nums[0]
min_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Max:", max_num)
print("Min:", min_num)



