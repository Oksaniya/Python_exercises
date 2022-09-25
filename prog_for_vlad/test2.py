import itertools
import numpy

f = open("/Users/oksana/Oksaniya/Python/prog_for_vlad/sample.txt", "r")
lst = []
comb = []
for x in f:
   lst.append(x)
#lst.sort()
mod = [eval(i) for i in lst]
fin_list = []
print(mod)
comb = list(itertools.combinations(mod, 5))
print(comb)

sum_list = [sum(l) for l in comb]
print("sum of combinations:", sum_list, "\n")
n = numpy.mean(sum_list)
print("mean of sum:", n)

i = 0
#e = 0
while (i < (len(sum_list))):
    if (sum_list[i] == 27):
        fin_list.append(comb[i])
      #  e += 1
    i += 1
print("combinations with mean sum are:", fin_list)
#print(e)
fin_list = set([tuple(sorted(x)) for x in fin_list])
#set(tuple(sorted(i)) for i in fin_list)
#print(fin_list)

f.close()