t = int(input("Enter number of test cases:"))
output = []
for i in range(t):
    n = int(input("Enter number of boys or girls:"))
    boys = []
    girls = []
    print("Enter heights of", n ,"boys")
    for i in range(n):
        boys.append(int(input()))
    print("Enter heights of", n ,"girls")
    for i in range(n):
        girls.append(int(input()))    
    boys.