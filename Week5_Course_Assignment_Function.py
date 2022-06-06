# Introduction to Python Programming
# Lesson 05 Assignment
# Sample Solutiondef convert_to_fahrenheit(celsius):

def convert_to_fahrenheit(celsius):
    """This function converts a Celsius temp to a Fah temp"""
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit

for cel in range(0, 101, 10):
    # The \t here is used to insert a Tab into the output
    print (cel, "\t", convert_to_fahrenheit(cel))
