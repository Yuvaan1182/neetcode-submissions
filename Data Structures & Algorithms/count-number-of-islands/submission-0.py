class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()
        res = []

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in vis or
                grid[r][c] == "0"
                ):
                return;
            
            vis.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in vis and grid[r][c] == "1"):
                    dfs(r, c)
                    temp = vis
                    res.append(list(vis))
        
        return len(res)



