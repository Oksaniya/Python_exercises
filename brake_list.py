def chunks(lst, n):
       for i in range(0, len(lst), n):
              yield(lst[i:i + n])

# driver part
lst = ['geeks', 'for', 'geeks', 'like',
       'geeky','nerdy', 'geek', 'love',
       'questions','words', 'life']
n = 5
print(list(chunks(lst,n)))
