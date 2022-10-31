(students, subjects) = tuple([int(x) for x in input().split(' ')])

sub_lines = []
for x in range(subjects):
    line = [float(num) for num in input().split(' ')]
    sub_lines += [line]

grades = zip(*sub_lines)
for student in grades:
    avg = sum(student)/subjects
    print(f'{avg:0.2f}')