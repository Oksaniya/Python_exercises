def minimal(tab):
    i = 0
    buf = tab[0]
    while(i < len(tab)):
        if(tab[i] < buf):
            buf = tab[i]
        i += 1
    return buf

def min2(tab):
    res = min(tab)
    return res

# driver code
tab = [11,2,3,4,77,7]
#res = minimal(tab)
res = min2(tab)
print("Minimal res is", res)
