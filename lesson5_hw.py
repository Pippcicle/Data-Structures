import random
mylist = [random.randint(1,1000) for _ in range(6)]


n = len(mylist)
for i in range(n):
    for j in range(0,n - i - 1):
        if (mylist[j] % 10) > (mylist[j+1] % 10): 
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)