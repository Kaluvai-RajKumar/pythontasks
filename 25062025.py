n = 153
org = n
temp = n
pw = 0

while temp > 0:
    temp = temp // 10
    pw += 1

sum = 0
temp = n
while temp > 0:
    ld = temp % 10
    sum += ld ** pw
    temp = temp // 10

print(sum)
if sum == org:
    print("Armstrong")
else:
    print("Not an Armstrong")

list1 = [4, 7, 1, 2, 8, 9, 10, 1, 3]
max = list1[0]

for num in list1:
    if num > max:
        max = num

print(max)
