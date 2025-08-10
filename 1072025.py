for n in range(1,11):
    x=n+1
    i=1
    is_square = False
    while i * i <= x:
        if i * i == x:
            is_square = True
            break
        i += 1
    if is_square:
        print(n)


for i in range(1,6):
    print(i*i)


count = 0
num=1
while count < 5:
    sum = 0
    for j in range(1,num):
        if num % j ==0:
            sum += j
    if sum == num:
        print(num)
        count += 1
    num += 1
