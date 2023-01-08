new_list = [10, 20, 30, 40, 50]


def addition(n):
    return n + 5


my_list = map(addition, new_list)
print(my_list)

for item in my_list:
    print(item)


def adding(x, y):
    return x + y

my_list = map(adding, ('apple ', 'watermalen '), ('banana', 'cherry'))
print(tuple(my_list))

new_list = [5, 10, 15, 20, 25, 30]
cube_n = map(lambda n: n**3, new_list)
print(list(cube_n))

num1 = [10, 20, 30]
num2 = [40, 50, 60]

new_result = map(lambda a, b: a*b, num1, num2)
print(list(new_result))