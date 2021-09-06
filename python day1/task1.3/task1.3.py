import math as ma
import time as t
def prime():
    try:
        n=int(input())
        for i in range(1,n+1):
            if i>1:
                for j in range(2,int(ma.sqrt(i))+1):
                    if i%j==0:
                        break
                else:
                    print(i)
                    t.sleep(5)
    except:
        print("exception")

prime() 
