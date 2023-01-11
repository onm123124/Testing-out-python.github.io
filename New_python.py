import random

# Generate a list of 10 random numbers between 1 and 10
numbers = random.sample(range(1, 11), 10)

# Add a duplicate to the list
numbers.append(numbers[0])
random.shuffle(numbers)

# Create a dictionary to store the count of each number
count = {}
for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

# Find the duplicate number
duplicate = None
for number, number_count in count.items():
    if number_count > 1:
        duplicate = number
        break

# Print out the final list of numbers and the duplicate number
print("The numbers are: ", ', '.join(map(str,numbers)))
print("The duplicate number is:", duplicate)
