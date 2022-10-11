l = 2
h = 3

i = 1
lst = []
sub = []
result = []
l_lst = l * h

while(i <= l_lst):
    lst.append(i)
    i += 1

for i in lst:
    sub += [i]
    if(len(sub) == l):
        result += [sub]
        sub = []

for i in result:
    print(i)