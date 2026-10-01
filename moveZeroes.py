n = int(input("Enter how many Array Elements: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Element "+str(i+1)+": "))
    arr.append(num)
print("Original Array: ",arr)

newArray = []
for i in range(n):
    if arr[i]!=0:
        newArray.append(arr[i])

for i in range(n):
    if arr[i]==0:
        newArray.append(arr[i])

print("Array After moving zeroes to the end: ",newArray)