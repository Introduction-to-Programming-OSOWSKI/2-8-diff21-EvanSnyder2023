def diff21(n):
    if abs (21 >= n):
        return abs (21 - n)
    elif abs (21 < n):
        return abs (n - 21)
    elif abs (n > 21):
        return abs (21 - n * 2)

        print(diff21(19))
