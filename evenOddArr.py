n = int(input("Enter How many Elements in Array: "))
arr = []
for i in range(n):
    num = int(input("Enter Array Element "+str(i+1)+": "))
    arr.append(num)
print(arr)

evenArr=0
oddArr=0
even=[]
odd = []
for i in range(n):
    if arr[i]%2==0:
        evenArr = evenArr+1
        even.append(arr[i])
        
    else:
        oddArr = oddArr +1
        odd.append(arr[i])

print(evenArr)
print(oddArr)
print(even)
print(odd)