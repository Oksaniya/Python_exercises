n = "1634"
l = len(n)
i = 0
import array as arr
m = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
while(i < l):
    m[i] = (ord(n[i]) - 48) ** l
    i = i + 1
i = 0
res = 0
while(i < l):
    res = res + m[i]
    i = i + 1
if(res == int(n)):
    print("Yes,", n, "is an Armstrong number")
else:
    print("No,", n, "isn't an Armstrong number")

