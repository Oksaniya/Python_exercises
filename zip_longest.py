from itertools import zip_longest

test_list = [["Gfg", "good"], ["is", "for"], ["Best", "no"]]
res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue ="")]
print(res)
