import numpy as np

# listica = [1,3,5]
# matriz = np.array([2,4,6])
# listica.append(7)
# matriz += np.array([8])
# print(listica)
# print(matriz)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# suma = a*b
# print(suma)


graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}

def dfs_non_recursive(graph, source):

    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]

    while(len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)

        if s not in graph:
            #leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)


DFS_path = dfs_non_recursive(graph, "A")
print(DFS_path)