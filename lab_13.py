def sub_lists (list):
    lists = [[]]
    for i in range(len(list) + 1):
        for j in range(i):
            lists.append(list[j: i])
    return lists
 

l = [1, 2, 3]
print(l)
print(sub_lists(l))
