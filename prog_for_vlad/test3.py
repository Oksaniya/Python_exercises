from itertools import permutations

f = open("/Users/oksana/Oksaniya/Python/prog_for_vlad/sample.txt", "r")
lst = []
comb = []
for x in f:
   lst.append(x)
#lst.sort()
mod = [eval(i) for i in lst]
print(mod)
comb = list(permutations(mod))
print(comb)


f.close()