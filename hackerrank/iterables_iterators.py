from itertools import combinations

n = input()
letters = input()
k = input()

letters = letters.split(' ')
combs = combinations(letters,int(k))

a_count = 0
tot_count = 0
for comb in combs:
    tot_count += 1
    if 'a' in comb:
        a_count += 1
print(f'{a_count/tot_count:0.3f}')