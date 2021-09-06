import sys
import re
import uuid
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
    f.write("-".join(l))
