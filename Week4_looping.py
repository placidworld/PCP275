# General for loop
for i in range(0, 10):
    print("~~~", i, "~~~")
    for j in range(0, 10):
        print(i * j)
    print()


# For loop with break
for number in range(1, 11):
    if number == 4:
        break
    print(number)
    
print("Thanks!")


# For loop with continue
for number in range(1, 11):
    if number == 4:
        continue
    print(number)

print("Thanks!")


# for loop with continue
for number in range(1, 11):
    if number == 4:
        continue
    print(number)
else:
    print("Existed normally")


# for loop with break
for number in range(1, 11):
    if number == 4:
        break
    print(number)
else:
    print("Existed normally")


# Additional sample
phrase = input("Please enter a phrase: ")
letter = input("Please enter a letter: ")
length = len(phrase)

for index in range(0, length):
    if phrase[index] == letter:
        print("The letter frist appears at index: ", index)
        break
else:
    print("Your letter wasn't found")
