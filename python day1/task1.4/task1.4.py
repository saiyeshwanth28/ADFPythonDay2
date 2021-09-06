def GCD(x, y):
    try:
        while(y):
            x,y = y,x % y
        return x
    except:
        print("exception occurred")  
a=int(input("Enter num 1 "))
b=int(input("Enter num 2 "))
print ("gcd or hcf is ",GCD(a,b))
