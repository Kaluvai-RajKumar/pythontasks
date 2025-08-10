n=1234
rev=0
while n>0:
    digit = n%10
    rev = rev *10+digit
    n=n//10
print(rev)

# Check if a Number is Prime
# Input: 7 → Output: True

n=7
for i in range(2,n):
    if n%i == 0:
        break
    else:
        print("True")

# Find the Factorial of a Number
# ➤ Input: 5 → Output: 120
n=5
fact=1
for i in range(1,6):
    fact = fact*i
print(fact)

# Check if a String is a Palindrome
# ➤ Input: 'madam' → Output: True
str1="Madam"
rev=''
for i in range(len(str1)-1,-1,-1):
    rev = rev + str1[i]
if str1 == rev:
    print("True")
else:
    print("False")

# Find the Sum of Digits of a Number
# ➤ Input: 123 → Output: 6

n=123
sum=0
while n>0:
    digit=n%10
    sum = sum + digit
    n=n//10
print(sum)

# Fibonacci Series up to N Terms
# ➤ Input: 5 → Output: 0 1 1 2 3
n = 5
a, b = 0, 1
for i in range(n):
     print(a)
     a, b = b, a + b

# Check if a Number is an Armstrong Number
# ➤ Input: 153 → Output: True
num=153
n=len(str(num))
sum=0
for i in str(num):
    sum += int(i)**n
if sum == num:
    print("True")
else:
    print("False")

# Count Vowels in a String
# ➤ Input: 'hello' → Output: 2
str1= "hello"
count=0
if str1 in ("aeiouAEIOU"):
    count += 1
print(count)
# Find the Largest Element in a List
# ➤ Input: [10, 30, 50, 40] → Output: 50
ip=[10,20,50,40,70,30]
max=ip[0]
for i in ip:
    if(i>max):
        max=i
print(max)
# Sort a List Without Using sort()
# ➤ Input: [4, 2, 5, 1] → Output: [1, 2, 4, 5]
n = [4, 2, 5, 1]
for i in range(len(n)):
    min_index = i
    for j in range(i + 1, len(n)):
        if n[j] < n[min_index]:
            min_index = j
    n[i], n[min_index] = n[min_index], n[i]
print(n)

# Check if Two Strings are Anagrams
# ➤ Input: 'listen', 'silent' → Output: True
str1 = 'listen'
str2 = 'silent'
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)

# Count the Frequency of Each Character in a String
# ➤ Input: 'aabbc' → Output: {'a': 2, 'b': 2, 'c': 1}
str1="aabc"
dict1={}
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

# Remove Duplicates from a List
# ➤ Input: [1, 2, 2, 3, 4, 4] → Output: [1, 2, 3, 4]
a=[1,2,2,3,4,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


# Find the Second Largest Number in a List
# ➤ Input: [1, 3, 4, 2] → Output: 3
numbers = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers[1])  

# Check if a Year is a Leap Year
# ➤ Input: 2020 → Output: True  in easy
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)