# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]

def join_elem(lst, n):
    res_lst = []
    i = 0
    res_lst.append(n)
    while(i < len(lst)):
        e = 1
        while(e < len(lst[i])):
            if(lst[i][0] == n):
                res_lst.append(lst[i][e])
            e += 1
        i += 1
    res_lst = tuple(res_lst)
    return res_lst

def first_numbers(lst):
    first_numb_lst = []
    for i in lst:
        first_numb_lst.append(i[0])
    return first_numb_lst

def uniq_first_numbers(first_numb_lst):
    uniq_first_numb_lst = []
    i = 0
    while(i < len(first_numb_lst)):
        if(check_uniq(uniq_first_numb_lst, first_numb_lst[i]) == True):
            uniq_first_numb_lst.append(first_numb_lst[i])
        i += 1
    return tuple(uniq_first_numb_lst)

def check_uniq(uniq_first_numb_lst, n):
    res = True
    i = 0
    while (i < len(uniq_first_numb_lst)):
        if(n == uniq_first_numb_lst[i]):
            res = False
        i += 1
    return res

# driver_code
lst = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13), (5, 70)]
print("Original list: ", lst)
res_lst = []
first_numb_lst = first_numbers(lst)
uniq_first_numb_lst = uniq_first_numbers(first_numb_lst)
print("Uniq first numbers: ", uniq_first_numb_lst)
for n in uniq_first_numb_lst:
    res_lst.append(join_elem(lst, n))
print("Result: ", res_lst)


