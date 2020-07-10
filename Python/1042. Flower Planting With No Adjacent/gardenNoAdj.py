"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
"""


def gardenNoAdj(N,paths):
    #build the matrix
    adjMatrix = {n:set() for n in range(1,N+1)}
    for path in paths:
        start = path[0]
        end = path[1]
        adjMatrix[start].add(end)
        adjMatrix[end].add(start)

    #Dictionary for garden to plant number
    gardenToPlant = {start:None for start in range(1,N+1)}
    seen = set()
    def DFS(root,prev=None):
        vals = {1,2,3,4}
        if root not in seen:
            seen.add(root)
            for val in vals:
                if gardenToPlant[root]==None and val!=prev and not any(val==gardenToPlant[neighbor] for neighbor in adjMatrix[root]):
                    gardenToPlant[root]=val
                    print(root,"---->",val)


            for neighbors in adjMatrix[root]:
                DFS(neighbors,gardenToPlant[root])
    for start in gardenToPlant:
        DFS(start)
    output = [0]*(N+1)
    for start in gardenToPlant:
        output[start] = gardenToPlant[start]

    print(output)
    return output[1:]
    

    # dic = {}
        # result = [0]*N
        # for path in paths:
        #     if path[0] not in dic:
        #         dic[path[0]] = [path[1]]
        #     else:
        #         dic[path[0]].append(path[1])
        #     if path[1] not in dic:
        #         dic[path[1]] = [path[0]]
        #     else:
        #         dic[path[1]].append(path[0])
        # garden_type = set((1,2,3,4))
        # for i in range(1,N+1):
        #     given = set()
        #     if i in dic:
        #         for j in dic[i]:
        #             if result[j-1] != 0:
        #                 given.add(result[j-1])
        #         possible_gargen = garden_type - given
        #         result[i-1] = possible_gargen.pop()
        #     else:
        #         result[i-1] = 1
        # return result
        
        
        answer = [0] * N
        
        # O(E)
        adj_map = defaultdict(set)
        for src, tgt in paths:
            adj_map[src].add(tgt)
            adj_map[tgt].add(src)  # since undirected connections
        
        # O(V + E)
        alternatives = defaultdict(lambda: set(range(1, 5)))
        for garden_idx in range(1, N+1):
            # pick first from left alternatives arbitrarily
            valid_color = list(alternatives[garden_idx])[0]
            answer[garden_idx-1] = valid_color
            
            # remove chosen color from alternatives of all neighbors
            for neighbor_idx in adj_map[garden_idx]:
                if valid_color in alternatives[neighbor_idx]:
                    alternatives[neighbor_idx].remove(valid_color)
                
        return answer

# print(gardenNoAdj(3,[[1,2],[2,3],[3,1]]))
gardenNoAdj(4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])

