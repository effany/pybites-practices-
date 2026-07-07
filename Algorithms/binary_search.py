from string import ascii_lowercase

def binary_search(sequence, target):
    if target in sequence:
        current_array = sequence.copy()
        while current_array:
            mid = len(current_array) // 2
            value = current_array[mid]
            if value == target:
                return sequence.index(target)
            elif value > target:
                current_array = current_array[:mid]
            else: 
                current_array = current_array[mid + 1:]





PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)
#print(binary_search(PRIMES, 18))
print(binary_search(ALPHABET, 'a'))