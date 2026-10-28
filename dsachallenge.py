# #Problem 1: Find the Largest Number in a List

# def find_largest(numbers):
#     if not numbers:
#         return None
#     largest_number = numbers[0]
#     for number in numbers:
#         if number > largest_number:
#             largest_number = number
#     return largest_number
# print(
#     f" largest Number: {find_largest([3, 41, 56, 21, 76, 9])} \n"
#     f"largest Number: {find_largest([-10, -5, -2, -18])} \n"
#     f"largest Number: {find_largest([])} \n"
# )

# # Problem 2: Find the Smallest Number in a List
# def find_smallest(numbers):
#     if not numbers:
#         return None 
#     smallest_number = numbers[0]
#     for number in numbers:
#         if number < smallest_number:
#             smallest_number = number
#     return smallest_number

# print(
#     f"Smallest number: {find_smallest([8, 3, 12, 1, 7])} \n"
#     f"smallest number: {find_smallest([-3, -10, -1, -6])}"
# )


# def list_sums(numbers):
#     if not numbers:
#         return None
#     total_sum = 0
#     for number in numbers:
#         total_sum += number
#     return total_sum

# print(
#     f"{list_sums([2, 4, 6, 8])}"
# )


#Problem 4: Count Even Numbers

def count_even_numbers(numbers):
    if not numbers:
        return None
    count_even = 0
    for number in numbers:
        if number % 2 == 0:
            count_even = count_even + 1
    return count_even

print(
    f"{count_even_numbers([1, 2, 3, 4, 6])}\n"
    f"{count_even_numbers([1, 3, 5, 7])}"
)

