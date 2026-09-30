n = int(input("Enter How many Elements in Array: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Elements"+str(i+1)+": "))
    arr.append(num)
print(arr)

newArr = list(set(arr))
newArr.sort()
print(newArr)

print("Largest Element is: ",newArr[-1])
print("Second Largest Element is: ",newArr[-2])
print("Smallest Element is: ",newArr[1])
print("Second Smallest Element is: ",newArr[2])