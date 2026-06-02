mylist = [3, 1, 2, 5, 4]
mylist.sort(reverse = True)
print(mylist)
mylist.sort(reverse = False)
print(mylist)

#Bubble Sort

mylist = [12, 34, 2, 5, 7]
for i in range (0, len(mylist)): 
    for j in range(i,len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)

#Insertion Sort
mylist = [12, 34, 2, 5, 7]
for i in range(0,len(mylist)): 
    minElement = 1000000000
    minLocation = -1

    for j in range (i, len(mylist)): 
        if minElement > mylist[j]:
            minElement = mylist[j]
            minLocation = j
    
    mylist[i], mylist[minLocation] = mylist[minLocation], mylist[i]

print(mylist)

