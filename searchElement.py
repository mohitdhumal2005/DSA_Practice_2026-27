n = int(input("Enter How Many Array Elements: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Element "+str(i+1)+": "))
    arr.append(num)
print(arr)

Ele = int(input("Enter Element to be searched in the Array: "))
if Ele in arr:
    print(Ele,"is Present in The Array ")
    print("Position: ",arr.index(Ele)+1)
else:
    print(Ele,"not Present in The Array ")