n = int(input("Enter How many Array Elements: "))
arr =[]
for i in range(n):
    num = int(input("Enter Array Elements "+str(i+1)+": "))
    arr.append(num)

print(arr)

uniqueArray = list(set(arr))
print("Array after Removing Duplicates: ",uniqueArray)
