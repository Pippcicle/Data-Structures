#Linear Search

numbers = [10,25,20,30,45,50]

target = int(input("Enter Target Number : "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target :
        print("Element found at index", i)
        found = True
        break
    if not found:
        print("Element not found at index", i)

print("-" * 40)
#Binary search
numbers = [10,20,30,40,50,60]
target = int(input("Enter target number : "))
left = 0 
right = len(numbers) - 1 
found = False
while left <= right : 
    mid = (left+right) // 2
    if numbers[mid] == target :
        print("Element found at index", mid)
        found = True
        break
    elif target < numbers[mid]: 
        right = mid-1
    else :
        left = mid + 1 

if not found :
    print("Element not found")

print("-" * 40)
#Finding students using linear search

student = ["Pippa", "Amelie", "Alex", "Jakub", "Max"]
target = input("Enter name to search : ")
found = False
for name in student :
    if name == target:
        print("Student found")
        found = True
        break

if not found:
    print("Student not found")