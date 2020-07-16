# https://leetcode.com/problems/student-attendance-record-i/

"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""
def checkRecords(s):
    call_count = {}

    for index in range(len(s)):
        call_count[s[index]] = call_count.get(s[index],0)+1
        if index>=2 and  s[index]=='L' and s[index-1]=='L' and s[index-2]=='L':
            return False
        if call_count.get('A',0)>1:
            return False
    return True
print(checkRecords("PPALLL"))
print(checkRecords("PPALLP"))
