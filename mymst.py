def mymst(arr):
    V = {}
    i = 0
    minc = 99999
    n_v = set()
    out = []
    for row in arr:
        if row[0] not in V:
            V[row[0]] = i
            n_v.add(row[0])
            i +=1
        if row[1] not in V:
            V[row[1]] = i
            n_v.add(row[1])
            i += 1
    l = len(V)
    graph = [[99999 for cal in range(l)] for row in range(l)]
    for row in arr:
        graph[V[row[0]]][V[row[1]]] = row[2]
        graph[V[row[1]]][V[row[0]]] = row[2]
    connectv = set()
    connectv.add(arr[0][0])
    n_v.remove(arr[0][0])
    while len(n_v) > 0:
        minc = 99999
        for pair1 in iter(connectv):
            for pair2 in iter(n_v):
                if graph[V[pair1]][V[pair2]] < minc:
                    minc = graph[V[pair1]][V[pair2]]
                    n1 = pair1
                    n2 = pair2
        out.append([n1,n2,minc])
        connectv.add(n2)
        n_v.remove(n2)
    return out










connection =[['A','B',1],
 	 ['B','C',4],
 	 ['B','D',6],
 	 ['D','E',5],
 	 ['C','E',1]]
print(mymst(connection))