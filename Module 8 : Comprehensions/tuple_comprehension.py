new_tuple = tuple(n for n in (1, 2, 3, 4))
print(new_tuple)

numbers = [1, 2, 3, 4, 5, 6, 7]
new_tuple = tuple(t for t in numbers if t % 2 == 0)

print(new_tuple)