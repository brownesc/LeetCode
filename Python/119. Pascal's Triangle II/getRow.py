"""
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
def getRow(index):
    triangle = { 0:[1],1:[1,1]}
    def helper(k,memo):
        if k not in memo:
            prev_row = helper(k-1,memo)
            row = []
            for num in range(k+1):
                if num in {0,k}:
                    row.append(1)
                else:
                    row.append(prev_row[num-1]+prev_row[num])
            memo[k]=row
            return row
        else:
            return memo[k]
    out=helper(index,triangle)
    print(out)
    return out


#Can do solution with only O(k) space
def getRow2(index):
    start =[1]
    for i in range(index):
        start.append(1)
        for j in range(i,0,-1):
            start[j]=start[j-1]+start[j]
    print(start)
    return start

getRow2(2)

