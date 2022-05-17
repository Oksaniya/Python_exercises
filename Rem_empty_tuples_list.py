# Remove empty tuples from a list
def rem(tuples):
    l = []
    for i in range(len(tuples)):
        if(tuples[i] != ()):
            l.append(tuples[i])
    return l
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(rem(tuples))