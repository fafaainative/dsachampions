

# # Problem 2: Find the Smallest Number in a List
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
