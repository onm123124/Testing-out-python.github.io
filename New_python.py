import random

# Generate a list of 10 random numbers between 1 and 10
numbers = random.sample(range(1, 11), 10)

# Add a duplicate to the list
numbers.append(numbers[0])
