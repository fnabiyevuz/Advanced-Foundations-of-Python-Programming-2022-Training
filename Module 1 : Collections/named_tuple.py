from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Fazliddin', '23', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
Point_2d = namedtuple('Point', ['x', 'y'])

new_point = Point_2d(50, 100)

print(new_point)
print(isinstance(new_point, Point_2d))
print(isinstance(new_point, tuple))

# unpacking tuple
x, y = new_point
print(f'{x}, {y}')

# index number
x = new_point[0]
y = new_point[1]
print(f'{x}, {y}')

# Iterate over new point
for item in new_point:
    print(item)

new_circle = namedtuple('new_circle', ['center_x', 'center_y', 'radius'], rename=True)

print(new_circle._fields)

# _make(), _asdict()

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
