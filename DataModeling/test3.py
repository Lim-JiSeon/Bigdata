# -*- encoding= cp949 -*-

import utils

temp = {}
fp, fn = utils.filePaths()
for p, n in zip(fp, fn): 
    words = utils.readFile(p, n)

dish = {}
fp, fn = utils.filePaths()
for p, n in zip(fp, fn): 
    text = utils.readFile(p, n)

    for line in text:
        if line not in dish:
            dish[line] = 1
    
    a = []
    for word in words:
        tt = word.split()
        word = tt[0]
        if len(tt) == 2:
            a.append(word)
        for d in list(dish.keys()):
            if word == d:
                continue
            if d.find(word) != -1:
                if word not in temp:
                    temp[word] = [d]
                    dish.pop(d)
                else:
                    temp[word].append(d)
                    dish.pop(d)

for i in a:
    temp.pop(i)

total_count = 0
for value_list in temp.values():
    total_count += len(value_list)

print(total_count)

print(1)