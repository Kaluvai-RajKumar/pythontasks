def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):   
        if num % i == 0:
            return False
    return True

op = {i: "Prime" for i in range(1, 21) if is_prime(i)}
print(op)
