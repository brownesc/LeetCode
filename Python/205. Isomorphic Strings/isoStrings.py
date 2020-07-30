# https://leetcode.com/problems/isomorphic-strings/
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


def isIsomorphic(s,t):
    def string_string_to_counter_list(s):
        string_to_int = {}
        count = 0 
        output = []
        for letter in s:
            if letter in string_to_int:
                output.append(string_to_int[letter])
            else:
                string_to_int[letter] = count
                count+=1
                output.append(string_to_int[letter])
        return output
    return string_string_to_counter_list(s) == string_string_to_counter_list(t)

print(isIsomorphic("as","ba"))
print(isIsomorphic("foo","bar"))
