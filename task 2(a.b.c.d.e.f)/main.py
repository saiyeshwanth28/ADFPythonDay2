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
    #print(l1)
    print('The word that was repeated maximum number of times:',l1.most_common(1)[0][0],end='\n')
    for i in l:
        if i.startswith("to"):
            c+=1
        elif i.endswith("ing"):
            c1+=1
        elif i==i[::-1] and len(i)>1:
            sample.write("palindrome is:"+i+'\n')
    sample.write("totals words with prefix 'to' are: "+ str(c)+'\n')
    sample.write("total words ending with 'ing' are: "+ str(c1)+'\n')

