from collections import OrderedDict

# create dict
new_dict = {'apple': 3, 'banana': 4, 'cherry': 7}
print(new_dict)

# empty ordered dict
new_ordered_dict = OrderedDict()
print(new_ordered_dict)

# ordered dict from regular dict
new_ordered_dict = OrderedDict(new_dict)
print(new_ordered_dict)

# add item to dictionary
new_ordered_dict['fig'] = 5
print(new_ordered_dict)

# replace item in a dict
new_ordered_dict['apple'] = 15
print(new_ordered_dict)

# delete values
new_ordered_dict.pop('cherry')
print(new_ordered_dict)

# moving the item
new_ordered_dict.move_to_end('apple')
print(new_ordered_dict)

# reverse iteration
for item in reversed(new_ordered_dict):
    print(item)

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)   