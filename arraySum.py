n = int(input("Enter Number of Elements in the Array: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Element "+str(i+1)+": "))
    arr.append(num)
print(arr)

sum=0
for i in range(n):
    sum = sum + arr[i]

print("Summation of array:",sum)