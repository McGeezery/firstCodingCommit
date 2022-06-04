#\n cause the start of a new line
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)
print("")

#\t tabs the spaceing
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print("")
#Backslash alone escapes the character that follows it
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

#Triple Quotes when using you dont have to escape single or double quotes
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
print("")

#Triple Quotes Python allows you to split strings over line without \n
anotherSplitString = """This string has been
split over 
several
lines"""

print(anotherSplitString)
print("")
#Triple Quotes you can also escape the split line that triple quotes is capable of creating
andAnotherSplitString = """This string has been \
split over \
several \
lines, \
but is now back on the same line due to the backslash"""

print(andAnotherSplitString)
print("")

#Using backslash and or \n \t \u is possible if you escape the backslash with another backslash
print("c:\\Users\\tom\\notes.txt")

#Using r before the string creates a raw string which treats \ as a character
print(r"c:\Users\tom\notes.txt")
