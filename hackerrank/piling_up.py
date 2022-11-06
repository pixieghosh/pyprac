def can_pile(cubes):
    cubes = deque(cubes)
    stack = list()
    while len(cubes) >= 1:
        first = cubes[0]
        last = cubes[-1]
        maximum = max(first,last)
        if len(stack) == 0:
            stack.append(maximum)
            if maximum == first:
                cubes.popleft()
            else:
                cubes.pop()
        else:
            if maximum > stack[-1]:
                return False
            else:
                stack.append(maximum)
                if maximum == first:
                    cubes.popleft()
                else:
                    cubes.pop()
    return True

num_cases = input()
for case in int(num_cases):
    length = input()
    cubes = [int(itm) for itm in input().split(' ')]
    print('Yes' if can_pile(cubes) else 'No')