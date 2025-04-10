# print("Hello World!\nGoodbye World!")
# print("Hello World!" + "Goodbye World!")
# print("Hello World!" + " " + "Eat more Panda!")
#
# print("Hello " + input("What is your name?\n") + "!")
from operator import length_hint
from xml.etree.ElementTree import tostring

# name = input("What is your name?\n")
# print(name)

name = input("What is your name?")
length = str(len(name))
print("Hi " + name + ", your name is " + length + " charachters long!")