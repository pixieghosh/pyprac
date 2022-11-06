from itertools import groupby

l = [1,1,1,2,2,2,3,3,3,4,5,5,6]

for (key,val) in groupby(l):
    print(key)
    print(len(list(val)))

s = input()
new_s = ''
for (key,val) in groupby(s):
    new_s += f'({len(list(val))}, {key}) '
print(new_s)