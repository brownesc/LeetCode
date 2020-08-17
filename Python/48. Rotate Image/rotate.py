# https://leetcode.com/problems/rotate-image/

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
def rotate(matrix):        
    # num_rows = len(matrix)
    # #Iterate through main diagonal and switch row/column indices
    # start = 0
    # while  start< num_rows-1:
    #     nr,nc = start+1,start+1
    #     while nr<num_rows:
    #         matrix[nr][start],matrix[start][nc] = matrix[start][nc], matrix[nr][start]
    #         nr+=1
    #         nc+=1
    #     start+=1
    # # return matrix
    # #Now rotate 
    # for i in range(len(matrix)):
    #     start = 0 
    #     last = len(matrix[i])-1
    #     while start<last:
    #         matrix[i][start],matrix[i][last] = matrix[i][last],matrix[i][start]
    #         start+=1
    #         last-=1
    # return matrix
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            print(matrix)
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))