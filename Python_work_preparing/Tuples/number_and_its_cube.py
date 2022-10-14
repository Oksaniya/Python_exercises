# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]
lst = [1, 2, 3]
new_lst = []
for i in lst:
    new_lst.append(i)
    new_lst.append(i*i*i)

sub = []
result = []
for i in new_lst:
    sub += [i]
    if(len(sub) == 2):
        result += [sub]
        sub = []

tuple_res = [tuple(l) for l in result]
print(tuple_res)