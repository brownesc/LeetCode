# https://leetcode.com/problems/number-of-islands/
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is 
formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def numIslands(grid):
    R = len(grid)
    C = len(grid[0])
    seen = set()
    count = 0 
    def onBoard(x,y):
        if 0<=x<R and 0<=y<C:
            return True
        else:
            return False
    
    def local_bfs_search(r,c,seen):
        seen.add((r,c))
        for nr, nc in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
            if onBoard(nr,nc) and grid[nr][nc]=="1" and (nr,nc) not in seen:
                local_bfs_search(nr,nc,seen)
    for r in range(R):
        for c in range(C):
            if grid[r][c]=="1" and (r,c) not in seen:
                local_bfs_search(r,c,seen)
                count+=1
    return count

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

                


        
        