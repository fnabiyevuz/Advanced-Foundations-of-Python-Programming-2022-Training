def new_generator():
    x = 0
    print("First point")
    yield x
    x += 1
    print("Second point")
    yield x
    x += 1
    print("Third point")
    yield x


new_ob = new_generator()
print(new_ob)

# print(next(new_ob))
# print(next(new_ob))
# print(next(new_ob))

for i in new_ob:
    print(i)

# use generator expression
new_list = [i * i for i in range(12)]  # using list comprehension
new_generator = (i * i for i in range(0, 12))

print(new_list)
print(new_generator)

for num in new_generator:
    print(num)


# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(next(x))  # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)
