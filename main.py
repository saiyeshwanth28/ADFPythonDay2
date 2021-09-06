from collections import Counter
import sys
import re
import uuid
l=[]
with open(sys.argv[1],'r+') as sample:
    data=sample.readlines()
    for line in data:
        word = line.split()
        l.extend(word)
    print('Word dict with Key as counter index and value as the words :',dict(enumerate(l)),end='\n')
    print('list Unique Words:',list(set(l)),end='\n')
    c,c1,c3=0,0,0
    l1=Counter(l)
    print('The word that was repeated maximum number of times:',l1.most_common(1)[0][0],end='\n')
    for i in l:
        if i.startswith("to"):
            c+=1
        elif i.endswith("ing"):
            c1+=1
        elif i==i[::-1] and len(i)>1:
            sample.write("palindrome is:"+i+'\n')
    print("totals words with prefix 'to' are: "+str(c)+'\n')
    print("total words ending with 'ing' are: "+ str(c1)+'\n')
input_file = open('file', 'r')
l1 = list(input_file.read().split(' '))
l = []
for i in range(len(l1)):
    l.extend(re.split('a|e|i|o|u|A|E|I|O|U', l1[i]))
for i in range(len(l)):
    if len(l[i]) >= 3:
        l[i].replace(l[i][2], l[i][2].upper(), 1)
    if (i+1) % 5 == 0:
        l[i] = l[i].upper()
    l[i] = l[i].replace('\n', ';')
l = ' '.join(l).split()
unique_filename = str(uuid.uuid4())
unique_filename += '.txt'
with open(unique_filename, "x") as f:
    f.write(str(l)+'\n')
    f.write("-".join(l))


