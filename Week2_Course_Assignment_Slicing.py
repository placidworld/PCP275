# Lesson 02 Assignment

# Use your knowledge of string variables and input to write a program
# that demonstrates how slicing works. Have your program get a word or
# phrase from the user and two numbers.
# Use those two numbers to slice the string and print out that slice.


# Use input to get the phrase value
phrase = input("Please enter a phrase: ")

# Get the starting and ending positions you define (input)
startPos = int(input("Please enter the starting position: "))
endPos = int(input("Please enter the ending position: "))

# Print out the slice of the phrase
print(phrase[startPos:endPos+1])

# Or print out the character at the last position
print(phrase[len(phrase)-1:len(phrase)])

               
