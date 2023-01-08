from collections import Counter

# Counter with list
new_list = ['a', 'b', 'c', 'a', 'b', 'b', 'c', 'b', 'c']
print(Counter(new_list))

# Counter with str
new_str = 'Advanced Python kursiga xush kelibsiz!'
print(Counter(new_str))

# Counter with dict
new_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'd': 2}
print(Counter(new_dict))

# Counter with tuple
new_tuple = ('apple', 'banana', 'cherry', 'apple', 'apple', 'fig', 'banana')
print(Counter(new_tuple))

# empty Counter
_counting = Counter()
_counting.update('Hi, Python is fun')
print(_counting)

# delete item from Counter
new_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'd': 2}
del new_dict['d']
print(Counter(new_dict))