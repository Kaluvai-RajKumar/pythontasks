
# Problem: Write a function to check if a number is prime.
#  Input: 11 → Output: True

n=11
for i in range(2,n):
    if n%i==0:
        print("False")
        break
else:
    print("True")
   
# Problem: Write a function to check if two strings are anagrams.
#  Input: "listen", "silent" → Output: True
s1="listen"
s2="silent"
if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")

# 3.     Second Largest Element
#  Problem: Write a function to find the second largest number in a list.
# Note :With out using slicing
lst = [10, 20, 5, 8]
largest = second = -1 
for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)


# 2. Find Missing Numbers in Range
#  Input: List from 1 to n with missing numbers
#  Example: lst = [1,2,4,6] → Output: [3,5]

n=6
lst=[1,2,4,6]
op=[i for i in range(1,n) if i not in lst]
print(op)


# 1.     List Compression (Run Length Encoding)
# Input: [1,1,1,2,2,3] → Output: [(1,3), (2,2), (3,1)]

lst = [1, 1, 1, 2, 2, 3]
result = []
current = lst[0]
count = 1
for i in range(1, len(lst)):
    if lst[i] == current:
        count += 1
    else:
        result.append((current, count))
        current = lst[i]
        count = 1
result.append((current, count))
print(result)
