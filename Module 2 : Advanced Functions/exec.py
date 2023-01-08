print(exec('print("Hi, Python")'))

new_code = """x = 20
y = 15
print('x + y = ', x + y)"""
print(exec(new_code))

# insert_code = input('Enter Python code : ')
# print(exec(insert_code))

code = exec('print(dir())')
print(code)

from math import *

code = """x = sqrt(16)
print(x)"""

p_code = exec(code, {'sqrt': sqrt})
print(p_code)
