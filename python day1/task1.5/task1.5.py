def num():
    try:
        n = int(input("Enter an decimal value: "))
        print(bin(n), "in binary.")
        print(oct(n), "in octal.")
        print(hex(n), "in hexadecimal.")
    except:
        print("Exception occurred")
num()
