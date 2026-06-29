def is_armstrong(n: int) -> bool:
    length = len(str(n))
    sum = 0
    for d in str(n):
        sum += (int(d) ** length)
    return True if sum == n else False
    