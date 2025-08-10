
str1="Deepthisriyha"
op1=[str1[i] for i in range(0,len(str1),2)]
print(op1)

s= ["even_index", True, 3.4, 3+6j, "reverse"] 
print(s)


str1="PythoNFullStacK" 
upper_let=[i for i in str1 if i.isupper()]
lower_let=[j for j in str1 if j.islower()]
print(upper_let)
print(lower_let)

str1="DeEpThIsRiYhA"
a=str1.swapcase()
print(a)


a=[1,2,2,3,3,4,4,4,5,5,5]
l=[]
for i in a:
    if i not in l:
        l += [i]
print(l)


l=[2,9,4,99,11,366]
max = l[0]
min = l[0]
for i in l:
    if i > max:
        max=i
    if i < min:
        min=i
print(max)
print(min)


l=[1,-2,4,-6,7,-8,10,-17]
pos=[i for i in l if i >0]
neg=[i for i in l if i < 0]
print(pos)
print(neg)


a=[1,23,44,67,97,112]
odd=[a[i] for i in range(1,len(a),2)]
print(odd)


l=[2,4,6,7,90,23]
mul=1
for i in l:
    mul *= i
print(mul)


l=[2,5,6,8,10,11,16,20]
n=len(l)
for i in range(n):
    for j in range(0, n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

str1 = "Deepthisriyhanarapaneni"
result = ""
for i in str1:
    if i.isupper():
        result += '@' + i
    else:
        result += i
print(result)


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