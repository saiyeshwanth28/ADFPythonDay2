def application():
    try:
        name=input("Enter the name ")
        age=int(input("Enter the age "))
        gender=input("Enter the gender ")
        salary=float(input("Enter the salary "))
        state=input("Enter the state ")
        city=input("Enter the city ")
        print(name,age,gender,salary,state,city,sep="\n")
    except:
        print("Something went wrong")
application()
