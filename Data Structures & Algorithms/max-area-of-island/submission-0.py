class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        #want count to reset for each ISLAND, not each recursive dfs call

        def dfs(r,c):
            #tells function to use count var declared outside 
            nonlocal count
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if grid[r][c] == 0 or (r,c) in seen:
                return
            
            count += 1
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    #reset count before we call dfs 
                    count=0
                    dfs(r,c)
                    #compare with current maxArea
                    maxArea = max(count, maxArea)

        return maxArea
                    
