
stu={}
while True:
    n=input("Enter a name (enter stop to finish )")
    if n.lower() == "stop":
        break
    marks=input(f"Enter marks for {n}: ")
    if marks.isdigit():
        stu[n] = int(marks)
    else:
        print("enter number")
print(stu)



n=[1,[2,3],[4,[5]]]
list1 = []
def flatns(n):
    for item in n:
        if isinstance(item, list):
            flatns(item) 
        else:
            list1.append(item)
flatns(n)
print(list1)


def most_frequent(lst):
    dict={}
    for i in lst:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    count = 0
    key=None
    for j in dict:
        if dict[j] > count:
            count = dict[j]
            key=j
    return key
lst=[2,3,5,5,6,5,7,8,5,7,5]
print(most_frequent(lst))

my_list=[]
def add_items():
    item = input("Enter a number to add: ")
    my_list.append(item)
    print("Added sucessfully")
def remove_item():
    item = input("Enter a number to remove")
    if item in my_list:
        my_list.remove(item)
        print("Removed")
    else:
        print("Not found")
def display():
    if my_list:
        print(my_list)
    else:
        print("U r list is empty")
while True:
    print("Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Exit")
    ip=input("Enter choice (1-4): ")
    if ip == '1':
        add_items()
    elif ip == '2':
        remove_item()
    elif ip == '3':
        display()
    elif ip == '4':
        print("Exit!")
        break
    else:
        print("Invalid choice.")


l1= [1, 3, 2, 2, 4, 0]
target=4
op=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]+l1[j] == target:
            op.append((l1[i],l1[j]))
print(op)
