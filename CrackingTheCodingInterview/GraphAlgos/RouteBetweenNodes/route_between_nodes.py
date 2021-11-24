from collections import deque

# O(e + v) | O(v) space
def path_between1(s, e, graph):
    q = deque()

    visited = set({})
    q.append(s)
    
    while len(q) > 0:
        curr = q.popleft()
        if curr == e:
            return True
        visited.add(curr)
        for child in graph[curr]:
            if child not in visited:
                q.append(child)

    return False

test_true = [[1, 2], [], [3], [4, 5, 6, 7], [], [], [3], [1]]
test_false = [[1, 2], [], [3], [4, 5, 7], [], [], [3], [1]]

test_true = {'a' : ['b', 'c', 'd'], 'b' : ['a']}

print(path_between1(0, 6, test_true))
print(path_between1(0, 6, test_false))