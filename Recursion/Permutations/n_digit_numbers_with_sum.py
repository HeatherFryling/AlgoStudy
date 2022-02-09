# Given n and a target sum,
# return the list of all n-digit
# numbers whose digits add up to
# the target sum.
def n_digit_numbers_with_sum(n, target):
    res = []
    path = []
    helper(n, target, 0, path, res)
    return res

def helper(n, target, total, path, res):
    if total > target:
        return

    # Note that here we have to keep track of two
    # conditions: Do we have the number of digits,
    # and have we summed to the target?
    if n == 0:
        if total == target:
            num = listToInt(path)
            res.append(num)
        return

    for i in range(10):
        if total == 0 and i == 0:
            continue
        path.append(i)
        helper(n - 1, target, total + i, path, res)
        path.pop()

def listToInt(ls):
    num = 0
    for d in ls:
        num *= 10
        num += d
    return num
assert([11, 20] == n_digit_numbers_with_sum(2, 2))
assert([14, 23, 32, 41, 50] == n_digit_numbers_with_sum(2, 5))
assert([104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500] == n_digit_numbers_with_sum(3, 5))