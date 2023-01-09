numbers = [100, 200, 300, 400, 500]
new_set = {s for s in numbers}

print(new_set)

new_set = {s ** 2 for s in numbers}
print(new_set)

print({n ** 2 for n in range(8)})

numbers = [1, 2, 3, 4, 5]
new_set = {s for s in numbers if s % 2 == 0}

print(new_set)