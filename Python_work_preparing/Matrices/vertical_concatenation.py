# Input :
# [[“Gfg”, “good”],
# [“is”, “for”]]
# Output : [‘Gfgis’, ‘goodfor’]




def make_plain_lst(matrix):
    lst_from_matrix = []
    for i in matrix:
        for e in i:
            lst_from_matrix.append(e)
    return lst_from_matrix


def sort_list(lst, l_elem_lst):
    sorted_lst = []
    i = 0
    while (i < len(lst)):
        if (i % l_elem_lst == 0):
            sorted_lst.append(lst[i])
        i += 1
    return sorted_lst


def remove_from_lst(lst_from_matrix, sorted_list):
    for i in lst_from_matrix:
        for e in sorted_list:
            if (i == e):
                lst_from_matrix.remove(i)
    return lst_from_matrix


def sublist(lst, l_fin_sublst):
    sub = []
    result = []
    for i in lst:
        sub += [i]
        if (len(sub) == l_fin_sublst):
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

matrix =    [["Gfg", "good"],
            ["is", "for"]]

l_elem_lst = len(matrix[0])
l_fin_sublst = len(matrix)

lst_from_matrix = make_plain_lst(matrix)
sorted_list = call_sort_and_remove(lst_from_matrix, l_elem_lst)
result = sublist(sorted_list, l_fin_sublst)

conc_lst = [''.join(sub_list) for sub_list in result]

for i in conc_lst:
    print(i)


