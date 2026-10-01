n = int(input("Enter how many Array Elements: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Element "+str(i+1)+": "))
    arr.append(num)
print(arr)

revArray = arr[::-1]
print("Original Array: ",arr)
print("Reverse Array: ",revArray)