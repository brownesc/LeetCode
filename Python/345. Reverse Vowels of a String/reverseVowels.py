# https://leetcode.com/problems/reverse-vowels-of-a-string/

"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

def reverseVowels(s):
    vowel_set = {'a','e','i','o','u','A','E','I','O','U'}
    vowel_order = []
    for index in range(len(s)):
        if s[index] in vowel_set:
            vowel_order.append(s[index])
    
    output = ""
    backwards_index = len(vowel_order) - 1
    for letter in s:
        if letter in vowel_set:
            output+=vowel_order[backwards_index]
            backwards_index-=1
        else:
            output+=letter
    return output
print(reverseVowels("leetcode"))