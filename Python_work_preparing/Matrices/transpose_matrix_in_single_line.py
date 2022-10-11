# [1, 2]
# [3, 4]
# [5, 6]
#
# [1, 3, 5]
# [2, 4, 6]

def make_plain_lst(matrix1):
    lst_from_matrix = []
    for i in matrix1:
        for e in i:
            lst_from_matrix.append(e)
    return lst_from_matrix

def sort_list(lst, l_elem_lst):
    sorted_lst = []
    i = 0
    while(i < len(lst)):
        if(i % l_elem_lst == 0):
            sorted_lst.append(lst[i])
        i += 1
    return sorted_lst


def remove_from_lst(lst_from_matrix, sorted_list):
    for i in lst_from_matrix:
        for e in sorted_list:
            if(i == e):
                lst_from_matrix.remove(i)
    return lst_from_matrix

def sublist(lst, l_fin_sublst):
    sub = []
    result = []
    for i in lst:
        sub += [i]
        if(len(sub) == l_fin_sublst):
            result += [sub]
            sub = []
    return result

def call_sort_and_remove(lst_from_matrix, l_elem_lst):
    sorted_list = []
    while (l_elem_lst > 0):
        if (len(lst_from_matrix) > 0):
            lst_from_matrix = remove_from_lst(lst_from_matrix, sorted_list)
            sorted_list += sort_list(lst_from_matrix, l_elem_lst)
        l_elem_lst -= 1
    return sorted_list

# driver code:

matrix1 =   [[1,2],
            [3,4],
            [5,6]]

l_elem_lst = len(matrix1[0])
l_fin_sublst = len(matrix1)

lst_from_matrix = make_plain_lst(matrix1)
sorted_list = call_sort_and_remove(lst_from_matrix, l_elem_lst)
result = sublist(sorted_list, l_fin_sublst)
for i in result:
    print(i)
