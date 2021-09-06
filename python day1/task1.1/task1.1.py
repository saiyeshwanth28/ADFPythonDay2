try:
    l=[]
    with open("E:\day 1 task 1.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            l.extend(word)
    l=sorted(list(set(l)),key=len)
    print(l)
    of=open("task11.txt",'w+')
    for i in l:
        of.write(str(i)+' '+str(len(i))+'\n')
    of.close()
except:
    print("Something went wrong")
