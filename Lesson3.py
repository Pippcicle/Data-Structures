# Fibonacci Series

def fibonacci(n):
    if n == 0 or n == 1 :
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(7):
    print(fibonacci(i))

#Factorial using resurion

def Factorial(n):
    if n == 1 :
        print("Reached base case")
        return 1
    else : 
        print("Calling Factorial(", n-1, ")")
        return n * Factorial(n-1)
    
print(Factorial(7))

#Sum of numbers till n using recursion

def  sumOfNo(n):
    print("Calling sumOfNo(", n , ")")
    if n == 1 or n == 0 :
        print("Base case reached with n = ",n)
        return n 
    else : 
        result = n + sumOfNo(n-1)
        print("Returning ", result," for n = ",n)
        return result
print ("Final Answer : ", sumOfNo(7))

#Power Function using Recursion

def Power(x,y):
    print("Calling Power (", x , ", ", y, ")")
    if y == 1 :
        print(f"Base case reached : power ({x}, 1) = {x}")
        return x
    else : 
        half = Power (x,y//2)
        if y % 2 == 0 :
            result = half * half
            print(f"Returning {result} for power ( {x}, {y})")
            return result
        else : 
            result = x * half * half
            print(f"Returning {result} for power ({x}, {y})")
            return result
        
print("Final Answer : ", Power(3,5))

#Countdown using recursion

def countdown(n):
    print(f"Calling countdown ({n})")
    if n == 0 : 
        print("Base case reached. Countdown finished")
        return
    else : 
        print("Current Number : ", n)
        countdown(n-1)
        print(f"Returning from countdown ({n})")

print("Starting countdown")
countdown(5)
print("Program ended")