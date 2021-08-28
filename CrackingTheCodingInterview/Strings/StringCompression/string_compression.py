# O(n) time | O(n) space
def string_compression(s):
    count_arr = []
    count_arr.append(s[0])
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            continue
        count_arr.append(str(count))
        count_arr.append(s[i])
        count = 1
    count_arr.append(str(count))
    ans = "".join(count_arr)
    print(ans)
    return ans if len(ans) < len(s) else s

test1 = "aabcccccaaa"
test2 = "abbbbba"
test3 = "bb"
test4 = "aaaaa"

print(string_compression(test1))
print()
print(string_compression(test2))
print()
print(string_compression(test3))
print()
print(string_compression(test4))
print()