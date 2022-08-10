# Lecture 1 - syntax

# print(1)
# int(9)
# int(999)
# print(2)
# print 3

# Lecture 2 - exceptions

# a = 1
# b = "2"
# print(int(2.5))
# print(a+b) - TypeError
# print(c) - NameError

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'You are dividing by zero'

print(divide(1,2))
print(divide(1,0))