#USER INPUT

# def weather_condition(temperature):
#     if temperature > 7:
#         return 'Warm'
#     else:
#         return 'Cold'

# # print(weather_condition(5))

# user_input = float(input('Enter temperature:'))

# print(weather_condition(user_input))


#STRING FORMATTING

# user_input = input('Enter your name: ')
# message = 'Hello %s!' % user_input
# message = f'Hello {user_input}!'
# print(message)

name = input('Enter your name: ')
surname = input('Enter your surname: ')
# message = 'Hello %s %s!' % (name, surname)
message = f'Hello {name} {surname}!'
print(message)