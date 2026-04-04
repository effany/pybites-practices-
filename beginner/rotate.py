def rotate(string, n):
    if not string:
        return ""

    n = n % len(string)
    new_word = ""
    for i in range(n, len(string)):
        new_word += string[i]
    for k in range(0, n):
        new_word += string[k]
    
    return new_word

rotate('julian and bob!', 100)

def rotate(string, n):
    if not string:
        return ""
    n %= len(string)
    return string[n:] + string[:n]