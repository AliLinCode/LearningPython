my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 4, 4, 4]

my_list_curent=[]


for i in my_list:
    if i not in my_list_curent:
        my_list_curent.append(i)


my_list=my_list_curent[:]
# Write your code here.
print("The list with unique elements only:")
print(my_list)
