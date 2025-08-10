for i in range(1,6):
    row=""
    for j in range(i):
        row+="*"
    print(row)

for i in range(1,6):
    row=0
    for j in range(1,i+1):
        row=row*10+j
    print(row)

row = ""
for i in range(1, 6):
    row += chr(96 + i)  
    print(row)
