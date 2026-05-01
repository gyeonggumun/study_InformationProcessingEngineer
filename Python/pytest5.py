def recur(n):
    if n <= 1:
        return 1
    else:
        # n이 짝수면 n + recur(n-1), 홀수면 n * recur(n-1)
        if n % 2 == 0:
            return n + recur(n-1)
        else:
            return n * recur(n-1)

print(recur(4)) # 4 + (3 * (2 + 1)) = 4 + (3 * 3) = 4 + 9 = 13
