def uniq_val(uniq_val_lst, val):
    res = True
    for i in uniq_val_lst:
        if(i == val):
            res = False
    return res

def val_count(val, val_lst):
    counter = 0
    for i in val_lst:
        if(i == val):
            counter += 1
    return counter

f = open("key-value.txt", "r")
text = f.read()
val_lst = text.split()
uniq_val_lst = [val_lst[0]]
for i in val_lst:
    if(uniq_val(uniq_val_lst, i) == True):
        uniq_val_lst.append(i)
for i in uniq_val_lst:
    print("The count of ", i, "is", val_count(i, val_lst))
