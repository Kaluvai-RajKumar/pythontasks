n = int(input("Enter a number: "))
x = n
l = len(str(n))
s = 0

while x > 0:
    d = x % 10
    s += d ** l
    x //= 10

if s == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
