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
