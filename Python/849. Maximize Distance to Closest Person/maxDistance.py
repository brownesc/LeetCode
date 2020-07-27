# https://leetcode.com/problems/maximize-distance-to-closest-person/

"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
 

Constraints:

2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
def maxDistToClosest(seats):
    #Intuition: Try iterating from the left fom left distance, from right for right distanc and take 
    #max(min(left_dist_array,right_dist_array))

    #left_iterate
    most_recent_seat = -1 
    min_distance = []
    for l_index in range(len(seats)):
        if seats[l_index]== 1:
            most_recent_seat = l_index
            min_distance.append(0)
        elif seats[l_index] == 0 and most_recent_seat == -1:
            min_distance.append(float("INF"))
        else:
            min_distance.append(l_index-most_recent_seat)
    
    most_recent_seat = -1
    print(min_distance)
    for r_index in range(len(seats)-1,-1,-1):
        if seats[r_index]== 1:
            most_recent_seat = r_index
            min_distance[r_index]=0
        elif seats[r_index] == 0 and most_recent_seat == -1:
            continue 
        else:
            min_distance[r_index] = min(min_distance[r_index],most_recent_seat-r_index)
    
    return max(min_distance)

print(maxDistToClosest([1,0,0,0,1,0,1]))
