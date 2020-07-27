# https://leetcode.com/problems/buddy-strings/

"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

def buddyStrings(A,B):
    if len(A)!=len(B):
        return False
    
    string1_A= -1
    string2_A= -1
    string1_B= -1
    string2_B= -1

    for i in range(len(A)):
        if A[i]!=B[i]:
            if string1_A ==-1:
                string1_A = A[i]
                string1_B = B[i]
            elif string2_B == -1:
                string2_A = A[i]
                string2_B = B[i]
            else:
                return False
    if string1_A==string2_B and string1_B == string2_A:
        return True
    elif string1_A == string1_B == string2_A == string2_B == -1:
        return True
    else:
        return False
print(buddyStrings("a","ab"))
print(buddyStrings("aab","aba"))
print(buddyStrings("abc","def"))

        