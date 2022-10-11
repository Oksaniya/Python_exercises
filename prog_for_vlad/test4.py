lst = [1.1, 3.5, 5.5, 5.5, 0, 6, -4.5, 6.7, 8.1, 0.6, 7.5, 6.2,9999999999999999.7, 9999999999999.86867744646657757, -9999999999999.7]
lst_mod = []
i = 1
buf_min = lst[0]
buf_max = lst[0]
while(i < len(lst)):
   if(buf_min > lst[i]):
      buf_min = lst[i]
   if (buf_max < lst[i]):
      buf_max = lst[i]
   i += 1
print(buf_min)
print(buf_max)
i = 0
while(i < len(lst)):
   if((lst[i] != buf_min) and (lst[i] != buf_max)):
      lst_mod.append(lst[i])
   i += 1

print(lst_mod)
i = 0
buf = 0
while(i < len(lst_mod)):
   buf += lst_mod[i]
   i += 1
print(buf)
print(sum(lst))
print(sum(lst) - buf_min - buf_max)