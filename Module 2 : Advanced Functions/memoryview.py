x = b'Python Programming'

new = memoryview(x)

print(type(new))
print(new)
print(new.obj)
print(new.tolist())

a = bytearray('Python is so powerful', 'utf-8')
print(type(a))

b = memoryview(a)
print(b)
print(b[4])
print(chr(b[4]))

new = b.tobytes()
print(type(new))

c = memoryview(b'45, 78, 98')
d = c[4]
print(d)
print(type(d))

x = memoryview(b'Hi, Python')
y = x[2:8]
print(y)
print(y.tobytes())
print(y.tolist())
print(list(y))