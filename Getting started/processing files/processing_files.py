location = "C:/Users/willi/Desktop/Programming/Python/Python Course/Getting started/processing files/"

#MANUAL OPEN AND CLOSE
# myfile = open(location + "fruits.txt")
# content = myfile.read()
# myfile.close()

#USING WITH
# with open(location + "files/fruits.txt") as myfile:
#     content = myfile.read()

# print(content[:2])
# print(content)

#WRITING FILES
# with open(location + "files/vegetables.txt", "w") as file:
#     file.write('Tomato\nCucumber\nOnion\n')
#     file.write('Garlic')

#WORKING WITH OTHER OPEN MODES
with open(location + 'files/fruits.txt', 'a+') as myfile:
    myfile.write('\nOkra')
    myfile.seek(0)
    content = myfile.read()

print(content)