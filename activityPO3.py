x = 5
print("X is 5")
if (type(x) is int):
    print("X is an Integer")
else:
    print("X is not an Integer")

x = 5.5
print("X is 5.5")
if (type(x) is not float):
    print("X is a Float")
else:
    print("X is not a Float")

x = 20
y = 20
print("X is 20. Y is 20")
if (x is y):
    print("X and Y has the same value")

y = 30
print("X is 20. Y is 30")
if (y is not x):
    print("X and Y do not have the same value")