number = 1

while number <= 5:
    print(number)
    number = number + 1
print("Goodbye!")


number = 1
answer = 'Y'

while answer == 'Y':
    print(number)
    number = number + 1
    answer = input("Do you want the next number? ")

num_of_nums = int(input("How many numbers do you want to average? "))

sum = 0.0

for count in range (num_of_nums):
    value = int(input("Enter a value: "))
    sum = sum + value

average = sum / num_of_nums

print("The average is: ", average)
