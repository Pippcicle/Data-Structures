def reverse_string(s):
    print(f"Calling reverse_string ({s})")
    if len(s) == 0 :
        print("Base case reached")
        return ""
    else : 
        result = s[-1]+reverse_string(s[:-1])
        print("Returning ", result )
        return result 

print("final answer : ", reverse_string ("Pippa"))
