def create_list(tab):
    i = 1
    lst_uniq = []
    lst_uniq.append(tab[i - 1])
    while(i < len(tab)):
        if (tab[i - 1] != tab[i]):
            lst_uniq.append(tab[i])
        i += 1
    return lst_uniq

def count_lst_create(tab, n):
    i = 0
    res = 0
    while(i < len(tab)):
        if(tab[i] == n):
            res += 1
        i += 1
    return res

def check_inc(lst_count):
    i = 1
    buf = lst_count[0]
    while(i < len(lst_count)):
        if(lst_count[i] > lst_count[i - 1]):
            buf = lst_count[i]
        i += 1
    return buf

# driver code
# which elem
tab = [1,1,2,2,1,1,3,3,3]
lst_uniq = create_list(tab)
i = 0
lst_count = []
while(i < len(lst_uniq)):
    lst_count.append(count_lst_create(tab, lst_uniq[i]))
    i += 1
buf = check_inc(lst_count)
print(lst_uniq[buf - 1])