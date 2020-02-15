structure = {'A': ['B', 'C'], 'B':['D', 'E'], 'C':['D','E'], 'D':['E'],'E': ['A']}
fullPath = []

def recursiveDFS (structure, nodeStart, fullPath):
    fullPath = fullPath + [nodeStart]
    print (fullPath)
    for node in structure[nodeStart]:
        if not node in fullPath:
            fullPath = recursiveDFS(structure, node, fullPath)
    return fullPath
print ('Recursive Depth First Search Result', recursiveDFS(structure, 'A', fullPath))

def iterativeBFS(structure, nodeStart, fullPath):
    x = [nodeStart]
    while x:
        print(x)
        firstNode = x.pop(0)
        if not firstNode in fullPath:
            fullPath = fullPath + [firstNode]
            x = x + structure[firstNode]
        return fullPath
print('Iterative Breadth First Search Result', iterativeBFS(structure, 'A', fullPath))