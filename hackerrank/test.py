def fib(num):
    nums = [1,1]
    while True:
        new_num = nums[-1]+nums[-2]
        if new_num > num:
            break
        else:
            nums.append(new_num)
    return nums
        
def solution(a):
    ret = []
    maximum = max(a)
    nums = fib(maximum)
    for val in a:
        if a in nums:
            ret.append(True)
        else:
            ret.append(False)
    return ret

solution([2,3,5])