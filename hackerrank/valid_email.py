from collections import Counter

def fun(s):
    counts = Counter(s)
    if counts['@'] != 1 or counts['.'] != 1:
        return False
    temp = s.split('@')
    parts = [temp[0]] + temp[1].split('.')
    if len(parts[0]) == 0 or len(parts[1]) == 0 or len(parts[2]) == 0:
        return False
    if len(parts[2]) > 3:
        return False
    for letter in parts[2]:
        if (ord(letter) not in range(ord('A'),ord('Z')+1)) and (ord(letter) not in range(ord('a'),ord('z')+1)) :
            return False
    for letter in parts[1]:
        if (ord(letter) not in range(ord('A'),ord('Z')+1)) and (ord(letter) not in range(ord('a'),ord('z')+1)) and (ord(letter) not in range(ord('0'),ord('9')+1)):
            return False
    for letter in parts[0]:
        if (ord(letter) not in range(ord('A'),ord('Z')+1)) and (ord(letter) not in range(ord('a'),ord('z')+1)) and (ord(letter) not in range(ord('0'),ord('9')+1)) and letter not in ['-','_']:
            return False
    else:
        return True
        
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)