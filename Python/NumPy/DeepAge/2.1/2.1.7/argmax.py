import numpy as np

a = np.random.randint(10, size=10)
print(a)
print("-" * 30)
print(np.argmax(a))
print("-" * 30)
print(a.argmax())
print("#" * 30)

b = np.random.randint(10, size=(3, 4))
print(b)
print("-" * 30)
print(np.argmax(b))
print("-" * 30)
print(b.argmax())
print("#" * 30)

print(b)
print("-" * 30)
print(np.argmax(b, axis=0))
print("-" * 30)
print(b.argmax(axis=0))
print("#" * 30)

print(np.argmax(b, axis=1))
print("-" * 30)
print(b.argmax(axis=1))
print("#" * 30)

c = np.random.randint(10, size=(2, 3, 4))
print(c)
print("-" * 30)
print(np.argmax(c, axis=0))
print("-" * 30)
print(c.argmax(axis=0))
print("-" * 30)
print(np.argmax(c, axis=1))
print("-" * 30)
print(c.argmax(axis=1))
print("-" * 30)
print(np.argmax(c, axis=2))
print("-" * 30)
print(c.argmax(axis=2))
