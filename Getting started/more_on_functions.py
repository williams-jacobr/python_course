# def area(a, b):
#     return a * b

# print(area(5, 4))

#ARBITRARY ARGUEMENTS
def mean(*args):
    return sum(args)/len(args)

print(mean(1, 3, 4))

#KEYWORD ARGUEMENTS
def dictionary(**kwargs):
    return kwargs

print(dictionary(a=1, b=2, c=3))