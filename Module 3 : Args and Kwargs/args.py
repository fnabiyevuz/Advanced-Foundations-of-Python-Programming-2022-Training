def addtition(*args):
    result = 0
    for x in args:
        result += x
    print(result)


addtition(10, 20, 30)
addtition(1, 2, 3, 4, 5)


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'Python course')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'Python course')
