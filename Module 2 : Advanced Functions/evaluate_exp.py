x = eval('10**3')
print(x)

print(sum([10, 20, 30, 40, 50]))

i = 10
print(eval('i*50'))

# global
x = 50
y = 20
print(eval('x+y', {'x': x, 'y': y}))

# local
print(eval('x+y', {}, {'x': 41, 'y': 15}))

expression = 'x*(x+1)*(x+2)'
print(expression)

x = 3

result = eval(expression)
print(result)

x = 5
print(eval('x == 4'))

x = None
print(eval('x is None'))

# check if element in tuple
chars = ('a', 'b', 'c')
print("'d' in chars tuple?", eval("'d' in chars"))

# check if number is greater or lesser
num = 100
print(num, "> 50?", eval('num > 50'))

# checking if number is even
num = 20
print(num, "is even?", eval('num % 2 == 0'))
