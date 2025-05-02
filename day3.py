n = int(input("Enter the number of operations"))
operations = []
print("Enter the", n ,"operations")
for i in range(n):
    operations.append(input())
stk = []
print(operations)
for i in range(n):
    if operations[i][0] == "A":
        temp = []
        temp = operations[i].split()
        stk.append(int(temp[1]))
    elif operations[i] == "Remove":
        if len(stk) == 0:
            print("Invalid")
        else:
            stk.pop()
    elif operations[i] == "CallMax":
        if len(stk) == 0:
            print("Invalid")
        else:
            print(max(stk))
    elif operations[i] == "CallMin":
        if len(stk) == 0:
            print("Invalid")
        else:
            print(min(stk))