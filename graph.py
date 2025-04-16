graph = {}

n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph[u] = graph.get(u, []) + [v]
    graph[v] = graph.get(v, []) + [u]

for node in sorted(graph):
    print(f'{node} {len(graph[node])}')
