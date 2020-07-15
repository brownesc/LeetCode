"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""

def numEquivDominoPairs(dominoes):
    # seen = set()
    count = 0
    total = {}
    for domino in dominoes:
        first = domino[0]
        sec = domino[1]
        if first<sec:
            if (first,sec) in total:
                total[(first,sec)]+=1
            else:  
                total[(first,sec)]=0
        else:
            if (sec,first) in total:
                total[(sec,first)]+=1
            else:
                total[(sec,first)]=0
    for duo in total:
        count+= (total[duo]**2+total[duo])//2
    return count

# print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))