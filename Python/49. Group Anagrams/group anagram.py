# https://leetcode.com/problems/group-anagrams/

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

def groupAnagrams(strs):
  word_dict = {}

  for word in strs:
    key = tuple(sorted(word))
    if key in word_dict:
      word_dict[key].append(word)
    else:
      word_dict[key] = [word]
  return list(word_dict.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sorted(["eat", "tea", "tan", "atefdfd", "nat", "bat"],key = lambda x:(-len(x),x)))