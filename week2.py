# --creating an empty list
my_list = []

# -- append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# --inserting 15 at index 1
my_list.insert(1, 15)

# -- extend my_list with[50, 60, 70]
my_list.extend([50, 60, 70])

# -- remove the last element from the list
my_list.pop()

# -- sort the list
my_list.sort()


# -- finding and printing the index of 30
print(f"The index of value 30 in my_list is {{{my_list.index(30)}}}")

# -- print the whole list
msg = f"my_list is {my_list}"
print()
print(msg)

