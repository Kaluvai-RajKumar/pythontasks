ef is_sunny(n):
    next_num = n + 1
    i = 1
    while i * i <= next_num:
        if i * i == next_num:
            return True
        i += 1
    return False




num = 8
print(is_sunny(num))


def is_neon(n):
    square = n * n
    digit_sum = 0
    while square > 0:
        digit_sum += square % 10
        square //= 10
    return digit_sum == n




num = 9
print( is_neon(num))