#FUNCTIONS

# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# print(mean([1,4,5]))

# def convert(amount):
#     output = amount * 1.75
#     return output

# print(convert(10))

#CONDITIONALS

def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)

    if isinstance(value, list):
        the_mean = sum(value) / len(value)

    return the_mean

student_grades = {'Mary': 9.1, 'Sim': 8.8, 'Joe': 7.5}

print(mean(student_grades))

x = 1
y = 3

def check(x,y):
    if x > y:
        return 'x is greater than y'
    elif x == y:
        return 'equal'
    else:
        return 'x is less than y'

print(check(x,y))

def foo(x ,array):
    if x in array:
        return True
    else:
        return False

print(foo(1, [1,2,3]))
print(foo(1, [2,3]))
print(foo(1, ['1',2,3]))