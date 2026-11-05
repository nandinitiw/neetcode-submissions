class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        islands = 0
        '''
        def dfs(r,c):
            #if we hit a node at the edge of the graph, stop
            #checks if any of r or c are out of bounds, then will just return
            if r>=rows or c>=cols or r<0 or c<0:
                return
            
            if grid[r][c]=="0" or (r,c) in seen:
                return 

            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        '''

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            queue = deque()
            #when we find new island, add starting coordinate to queue
            queue.append((r,c))
            seen.add((r,c))

            while queue:
                curr_r, curr_c = queue.popleft()
                #does bfs on each neighbor, one by one
                for dr, dc in directions:
                    new_r = curr_r+dr
                    new_c = curr_c+dc
                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                        #if one neighbor is out of bounds, still check the others
                        continue
                    elif grid[new_r][new_c]=="0" or (new_r, new_c) in seen:
                        continue
                    else:
                        seen.add((new_r,new_c))
                        queue.append((new_r,new_c))
                    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1

        return islands

        





        
