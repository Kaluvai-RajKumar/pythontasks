n=8
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(n)
else:
    a = n - 1
    b = n + 1

    is_a_prime = True
    for j in range(2, a):
        if a % j == 0:
            is_a_prime = False
            break
        if is_a_prime:
            print(a)
        break

    is_b_prime = True
    for k in range(2, b):
        if b % k == 0:
            is_b_prime = False
            break
        if is_b_prime:
            print(b)
            break