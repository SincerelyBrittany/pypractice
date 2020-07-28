from math import *

#imports more math functions

#first hello world

print("Hello World")

# first shape

print("My first shape is drawing a shape")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# variables - use underscore
character_name = "John"
character_age = "75"
integer = 75
isBoolean = True
floats = 50.040395

print("There once was a man named " + character_name + ",")
print("He was " + character_age + " years old")

#Updates the name
character_name = "Tom"
character_age = "50"
print("He really liked the name " + character_name)
print("but he did not ike being "+ character_age +".")

#working with strings in py

#inserts a new line
print("Sincerely\nBrittany")
#inserts a quotation
print("Sincerely\"Brittany")
#inserts a backslash
print("Sincerely\Brittany")

phrase = "Sincerely Brittany"
print(phrase)

#concatenate
print(phrase + "is awesome")


#functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

#length function
print(len(phrase))

#get individual characters ina string
print(phrase[2])

#passing a parameter
print(phrase.index("S")) #where the first "S" index is located
print(phrase.index("i"))
print(phrase.index("Brit"))

print(phrase.replace("Brittany", "Britt"))


#NUMBERS

print(3+4)
print(3 * 7.5)
print(3 * (4 + 5))

my_num = 3
print(my_num)

#convert into a string
print(str(my_num) + "my favorite number")

#absolute value
my_num = -5
print(abs(my_num))

#power
print(pow(3, 2))

#power
print(round(3.7))

#imported math functions
print(ceil(3.7))
print(floor(3.7))
print(sqrt(36))


#GETTING INPUT FROM A USER

# name = input("enter your name")
# age = input("enter your age")
# print("Hello " + name + "! You are " + age)


#Building a basic calculator
num1 = input("Enter a number ")
num2 = input("Enter another number ")

#results = num1 + num2 #- A STRING
# results = int(num1) + int(num2) #- A WHOLE NUM
results = float(num1) + float(num2) #- ENTER ANY NUMBER FLOAT FUNCTION
# results = int(num1) + int(num2)
print(results)


#MAD LIBS Example - 59:10