n=int(input("Enter"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)


str1="sriyha"
for char in range(len(str1)-1,-1,-1):
    print(str1[char])


str2="WOW"
s=""
for i in range(len(str2)-1,-1,-1):
    s+=str2[i]






d="good"
count=0
for char in d:
    if char in ("a","e","i","o","u"):
        count+=1
        print(count)
a=int(input("a: "))
b=int(input("b: "))
a,b=b,a
print(a)
print(b)


l1=[6,3,42,2,3,43,1,2,3,1,1,2]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


l1=[4,2,5,8,1,4,77,5,2]
smaller = l1[0]
l2=[]
for i in l1:
    if smaller < i:
        l2.append(i)
print(l2)
str1="race"
str2="care"
l1=[]
l2=[]
for i in str1:
    l1.append(i)
for j in str2:
    l2.append(j)
l1.sort()
l2.sort()
if l1 == l2:
    print("Anagram")
else:
    print("not")


sum=0
n=10
l1=[1,2,3,5,6,7,8,9,10]
for i in l1:
    sum += i
n1=n*(n+1)/2
print("Missing letter",n1-sum)


l1=[5,4,6,2,1,9,10]
l1.sort(reverse=True)
print(l1[1])


str1="Hello world welcome to 10000 coders"
str1.split(" ")
reversed_str=str1[::-1]
op = " ".join(reversed_str)
print(op)