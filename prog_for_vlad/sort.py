import itertools
import numpy

f = open("/Users/oksana/Oksaniya/Python/prog_for_vlad/batteries.txt", "r")
lst = []
comb = []
for x in f:
   lst.append(x)
lst.sort()
mod = [eval(i) for i in lst]

fin_list = []



#N = 8
#subList = [mod[n:n+N] for n in range(0, len(mod), N)]
sum_list = [sum(l) for l in comb]
print("sum of combinations:", sum_list, "\n")
n = numpy.mean(sum_list)
print("mean of sum:", n)
#print("Before combination:", subList)
print("\n")
comb = list(itertools.product(*subList))
print("Number combinations:", comb)
print("\n")
sum_list = [sum(l) for l in comb]
#print("sum of combinations:", sum_list)
print("\n")
n = numpy.mean(sum_list)
#print("mean of sum:", n)
print("\n")
i = 0
e = 0
while (i < (len(sum_list))):
    if (sum_list[i] == 18569):
        fin_list.append(comb[i])
        e += 1
    i += 1
#print("combinations with mean sum are:", fin_list)
print(e)
fin_list = set([tuple(sorted(x)) for x in fin_list])
#set(tuple(sorted(i)) for i in fin_list)
#print(fin_list)
listik = [2543, 2596, 2622, 2647, 2689, 2700, 2772]
#print(sum(listik))
#import random
#i = 0
#while (i < 5):
 #   random.shuffle(mod)
  #  comb.append(mod)
  #  i += 1
#print ("List after shuffle  : ",  comb)


#for L in range(0, len(mod)+1):
 #   for subset in itertools.combinations(mod, L):
  #      if (len(subset) == 4):
   #         comb.append(subset)
#print(comb)

#print("Modified list is: ", mod)

#N = 8
#subList = [mod[n:n+N] for n in range(0, len(mod), N)]
#new_list = [sum(l) for l in subList]

#print(new_list)
#print("\n")

#print(subList)
f.close()