def diff21(n):
    if 21 >= n:
        return 21 - n
    elif 21 <= n:
        return n - 21
    elif n > 21:
        return abs(n) * 2 - 21
