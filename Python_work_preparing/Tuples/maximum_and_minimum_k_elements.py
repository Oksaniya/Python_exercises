# Input : test_tup = (3, 7, 1, 18, 9), k = 2
# Output : (3, 1, 9, 18)

tp = (3, 7, 1, 18, 9)
k = 2
k2 = k
tp_lst = list(tp)
res_lst = []

def smallest_val(tp_lst):
    i = 1
    buf = tp_lst[0]
    while(i < len(tp_lst)):
        if(buf > tp_lst[i]):
            buf = tp_lst[i]
        i += 1
    for e in tp_lst:
        if(e == buf):
            tp_lst.remove(e)
    return buf

def biggest_val(tp_lst):
    i = 1
    buf = tp_lst[0]
    while(i < len(tp_lst)):
        if(buf < tp_lst[i]):
            buf = tp_lst[i]
        i += 1
    for e in tp_lst:
        if(e == buf):
            tp_lst.remove(e)
    return buf

while(k > 0):
    res_lst.append(smallest_val(tp_lst))
    res_lst.append(biggest_val(tp_lst))
    k -= 1

i = 0
sorted_res_lst = []
l_res = len(res_lst)

while(i < l_res):
    sorted_res_lst.append(smallest_val(res_lst))
    i += 1

print(sorted_res_lst)