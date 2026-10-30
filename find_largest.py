# #Problem 1: Find the Largest Number in a List

def find_largest(numbers):
    if not numbers:
        return None
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number
print(
    f" largest Number: {find_largest([3, 41, 56, 21, 76, 9])} \n"
    f"largest Number: {find_largest([-10, -5, -2, -18])} \n"
    f"largest Number: {find_largest([])} \n"
)

