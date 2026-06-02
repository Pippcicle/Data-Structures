words = ["apple", "kiwi", "banana", "pie", "date"]

for i in range(1, len(words)) : 
    key = words[i]
    j = i-1
    
    while j >= 0 and len(key) < len(words[j]):
        words[j+1] =  words[j]
        j-=1

    words[j+1] = key

print("Sorted by length : ", words)