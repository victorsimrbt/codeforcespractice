t = int(input())
for i in range(t):
    # tree = {}
    n = int(input())
    # tree[1]  = []
    adj = {i:[] for i in range(1,n+1)}
    readings = 0
    # edges = []
    queue = [[1,1]]
    visited = set()
    visited.add(1)
    for x in range(n-1):
        u,v = map(int,input().split())
        # print(u,v,adj[u],adj[v])
        if u in visited and not v in visited:
            queue.append([1,v])
            visited.add(v)
            
        adj[u].append(v)
        adj[v].append(u)
        
        # edges.append([u,v])
    print(visited)
    head = 0
    while head < len(queue):
        level,node = queue[head]
        states = adj[node]
        for state in states:
            if not state in visited:
                queue.append([level+1,state])
                visited.add(state)
        head += 1
    print(queue)
    readings = queue[-1][0]
        
    
    
    # while len(tree.keys()) != n:
    #     for edge in edges:
    #         u,v = edge
    #         #print(edge)
    #         if u in tree and not v in tree:
    #             #print("{} in list, {} is not".format(u,v))
    #             tree[u].append(v)
    #             tree[v] = [u]
    #     readings += 1
    #     #print(tree)
    print(readings)