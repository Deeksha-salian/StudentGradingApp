n = int(input("Enter the number of operations"))
operation = []
print("Enter the", n ,"operation")
for i in range(n):
    operation.append(input())
stk = []
print(operation)
for i in range(n):
    if operation[i][0] == "A":
        temp = []
        temp = operation[i].split()
        stk.append(int(temp[1]))
    elif operation[i] == "Remove":
        if len(stk) == 0:
            print("Invalid")
        else:
            stk.pop()
    elif operation[i] == "CallMax":
        if len(stk) == 0:
            print("Invalid")
        else:
            print(max(stk))
    elif operation[i] == "CallMin":
        if len(stk) == 0:
            print("Invalid")
        else:
            print(min(stk))
