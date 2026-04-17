def art_thief(paintings):
    if len(paintings) ==0:
        return 0
    elif len(paintings) <= 2:
        return max(paintings)
    dp = [0] * len(paintings)
    dp[0] = paintings[0]
    dp[1] = max(paintings[0], paintings[1])
    print(dp[1], 'dp[1]')
    print(dp, 'dp')
    for i in range(2, len(paintings)):
        dp[i] = max(dp[i-1], dp[i-2] + paintings[i])

    print(dp[-1])
    return dp[-1]

if __name__ == "__main__":
    art_thief([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   

