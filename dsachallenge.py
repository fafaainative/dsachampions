#Problem 1: Find the Largest Number in a List

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

# Problem 2: Find the Smallest Number in a List
def find_smallest(numbers):
    if not numbers:
        return None 
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(
    f"Smallest number: {find_smallest([8, 3, 12, 1, 7])} \n"
    f"smallest number: {find_smallest([-3, -10, -1, -6])}"
)
