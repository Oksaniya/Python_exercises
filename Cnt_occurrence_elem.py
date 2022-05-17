# Python | Count occurrences of an element in a list
def cnt(lst, x):
    e = 0
    for i in range(len(lst)):
        if(lst[i] == x):
            e += 1
    return e
# driver part
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(x, "occurs", cnt(lst, x), "times")