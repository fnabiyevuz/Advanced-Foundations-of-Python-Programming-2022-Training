def adding(num):
    return num + 1


adding_one = adding

print(adding_one(10))
print(adding_one(20))


def adding(num):
    def adding_one(num):
        return num + 1

    total = adding_one(num)
    return total


print(adding(15))
print(adding(25))


def adding(num):
    return num + 1


def calling(new_func):
    new_number = 10
    return new_func(new_number)


print(calling(adding))


# return a function from a function
def hello():
    def greating():
        return "Hi there"

    return greating


new_greating = hello()
print(new_greating)


# Closure
def new_message(text):
    """Outer message"""
    def another_message():
        """Our nested message"""
        print(text)
    another_message()

new_message('Hello, Python')


def new_capital(new_func):
    def new_inner():
        the_func = new_func()
        upper_case = the_func.upper()
        return upper_case
    return new_inner

def greating():
    return "Hi, Python Programming"

new_decorating = new_capital(greating)
print(new_decorating())

# the same as
@new_capital
def greating():
    return "Hi, Python Programming"

print(greating())