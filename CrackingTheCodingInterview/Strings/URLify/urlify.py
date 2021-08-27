
# O(n) time | O(1) space -- assuming there is space in the existing array for all the chars.
def urlify(s_list, l):
    sp = ' '
    num_sp = count_chars(s_list, l, sp)
    new_index = l - 1 + (num_sp * 2)

    # Finding the end of the new char array.
    if (new_index + 1 < len(s_list)):
        s_list[new_index] = '\0'

    for i in range(l - 1, -1, -1):
        if s_list[i] == sp:
            s_list[new_index] = '0'
            s_list[new_index - 1] = '2'
            s_list[new_index - 2] = '%'
            new_index -= 3
        else:
            s_list[new_index] = s_list[i]
            new_index -= 1
    
    return "".join(s_list)

def count_chars(s, l, target):
    count = 0
    for i in range(l):
        if s[i] == target:
            count += 1
    return count


test = list('Mr. John Smith      ')

print(list(test))
print(len('Mr. John Smith'))

print(urlify(test, 14))