# Regular way
fruits_list = ['fig', 'banana', 'kiwi', 'cherry']
my_list = []

for item in fruits_list:
    if 'i' in item:
        my_list.append(item)
print(my_list)

# Use List Comprehension
fruits_list = ['fig', 'banana', 'kiwi', 'cherry']
my_list = [item for item in fruits_list if 'e' in item]
print(my_list)

# Iterate over sequence with regular way
new_list = []  # empty list

for new_char in "Power of comprehension":
    new_list.append(new_char)
print(new_list)  # printing the List

# The same as
new_list = [new_char for new_char in "Power of comprehension"]
print(new_list)  # printing the List

# You can use nested List comprehension
new_matrix = []

for x in range(5):
    new_matrix.append([])  # adding empty sublist inside the list

    for y in range(8):
        new_matrix[x].append(y)
print(new_matrix)

# The same as
new_matrix = [[y for y in range(8)] for x in range(5)]
print(new_matrix)