class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        vis = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node in vis:
                return
            vis.add(node)

            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)

        cnt = 0

        for node in range(n):
            if node not in vis:
                print(node)
                dfs(node)
                cnt += 1
        
        return cnt