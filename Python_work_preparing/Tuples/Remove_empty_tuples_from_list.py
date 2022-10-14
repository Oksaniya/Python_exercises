# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
#                   ('krishna', 'akbar', '45'), ('',''),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('', '')]

def rem_empty_tup(tup):
    lst = []
    for i in tup:
        if(i != ()):
            lst.append(i)
    return lst


tup = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
lst = rem_empty_tup(tup)
print(lst)