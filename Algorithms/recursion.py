def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    if number < base:
        return number

    # Build the higher-order digits first, then append the current remainder digit.
    return dec_to_base(number // base, base) * 10 + (number % base)

print(dec_to_base(7,2))