def zeros(n):
    count = 0
    while n > 0:
        n = n // 5
        count += n
    return count


# test:
assert zeros(12) == 2

assert zeros(0) == 0
assert zeros(5) == 1
assert zeros(30) == 7
