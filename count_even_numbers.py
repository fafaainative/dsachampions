
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

