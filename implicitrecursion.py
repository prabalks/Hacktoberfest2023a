def find_largest(numbers):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest


def find_second_largest(numbers):

	# Remove the largest number from the list
	numbers.remove(find_largest(numbers))

	# Return the largest remaining number
	return find_largest(numbers)

# Driver code


numbers = [1, 2, 3, 4, 5]

# Function call
second_largest = find_second_largest(numbers)
print(second_largest)
