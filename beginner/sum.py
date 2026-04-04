def sum_numbers(numbers=None):
    if numbers is None:
        total = sum(range(101))
        print(total)
        return total

    if len(numbers) > 0:
        total = sum(numbers)
        print(total)
        return total

    print(0)
    return 0


sum_numbers()