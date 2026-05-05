def countdown(n):
    print(n)
    if n == 0 : 
        print("Blast Off!")
        return
    else : 
        countdown(n-1)
        
print("Starting countdown")
countdown(5)