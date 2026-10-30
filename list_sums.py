#function to sum list of numbers
def list_sums(numbers):
    if not numbers:
        return None
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

print(
    f"{list_sums([2, 4, 6, 8])}"
)
