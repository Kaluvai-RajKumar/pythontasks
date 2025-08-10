def factorial(num):
    fact=1
    for x in range(1,num+1):
        fact = fact * x
    return fact
def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if (num%i == 0):
            sum += i
    return sum == num
op={i:factorial(i) for i in range(1,7)}
print(op)