#Define Variable - a way to give a meaningful name to an area of memory, into which
# we can place certain values
# The type of variable is determined by python when you attach the value

# Example the value attached below is a string
greeting = "Hello"
print(greeting)\

#Space between lines - print("")
print("")

#Variables are case sensetive so the follow example is refering to another area of memory
Greeting = "Hello 2"
print(Greeting)

#Variables should start with a letter upper or lower case or the underscore character
# The equals sign = is how you assign the value to a variable

print("")

#This next line is a example of how to Bind user input to a variable
name = input("What is your name? ")
age = input("What is your age? ")
year = 2022
print("")
print("Well Hello " + ' ' + name + ', ' + "it's great to meet you!")
print("I see you are" + " " + age + " " + "years old. Wow that's old.")
print(name + " it is" + year + " after all.")
print("")

#How to get python to tell you what data Type of variable is bound
print(type(name))
print(type(age))
print(type(year))