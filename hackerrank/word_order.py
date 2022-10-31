num_lines = int(input())

words = []
for x in range(num_lines):
    word = input().rstrip('\n')
    words.append(word)

word_counter = Counter(words)

print(len(word_counter))
print(' '.join([str(word_counter[word]) for word in word_counter]))
