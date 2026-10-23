# For every u-v edge in a graph, return a ordering that all u appear before v
def topological_sort(V, adj: list[list[int]]):
    inDegree = [0] * V
    # calculate the inDegree of all nodes
    for i in range(len(adj)):
        for j in adj[i]:
            inDegree[j]+=1
    from collections import deque
    q = deque()

    for i in range(V):
        if inDegree[i] == 0:
            q.append(i)
    topo = []
    while q:
        i = q.popleft()
        topo.append(i)

        for j in adj[i]:
            inDegree[j]-=1
            if inDegree[j] == 0:
                q.append(j)

    return topo



