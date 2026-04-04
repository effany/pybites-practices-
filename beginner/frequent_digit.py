from collections import Counter
def freq_digit(num: int) -> int:
    digit_freq = Counter(str(num))
    if int(max(digit_freq, key=digit_freq.get)) == 1:
        return int(str(num)[0])
    else:
        return int(max(digit_freq, key=digit_freq.get))




print(freq_digit(12345))