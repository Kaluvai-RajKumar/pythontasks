s="welcom to 10000coders"
print(s[::-1])
s="welcom to 10000coders"
rev = ""
for i in s:
    rev = i + rev
print(rev)
s="MOM"
rev = ""
for i in s:
    rev = i + rev
if rev == s:
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a Palindrome")
str1="Python Programming"
s=str1.lower()
count = 0
for i in s:
    if i in "aeiou":
        count += 1
print(count)
str1 ="   Python Full Stack Developement  "
s = str1.strip()
print(s)
str2="Python is a object oriented programming language"
s=str2.split()
print(len(s))
str1="python program"
for i in str1:
    if str1.count(i) ==  1:
        print(i)
str1="PyThOn pRoGraM"
s=str1.swapcase()
print(s)






