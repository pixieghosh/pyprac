k = int(input())
peeps = [int(num) for num in input().split(' ')]

dct = {}
for peep in peeps:
    if peep not in dct:
        dct[peep] = 1
    else:
        dct[peep] += 1

for key in dct:
    if dct[key] == 1:
        print(key)

### ALTERNATIVELY

from collections import Counter

k = int(input())
peeps = [int(num) for num in input().split(' ')]
print(Counter(peeps).most_common()[-1][0])
