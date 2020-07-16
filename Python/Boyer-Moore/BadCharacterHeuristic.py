# Pattern searching is an important problem in computer science. When we do search for a string in notepad/word file or browser or database, pattern searching 
# algorithms are used to show the search results. A typical problem statement would be-

# Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
# You may assume that n > m.

"""
Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

Bad Character Heuristic

The idea of bad character heuristic is simple. The character of the text which doesn’t match with the current character of the pattern is 
called the Bad Character. Upon mismatch, we shift the pattern until –
1) The mismatch becomes a match
2) Pattern P move past the mismatched character.

Case 1 – Mismatch become match
We will lookup the position of last occurrence of mismatching character in pattern and if mismatching character exist in pattern then we’ll 
shift the pattern such that it get aligned to the mismatching character in text T.

Case 2 – Pattern move past the mismatch character
We’ll lookup the position of last occurrence of mismatching character in pattern and if character does not exist we will shift pattern past the 
mismatching character.

"""

# Python3 Program for Bad Character Heuristic 
# of Boyer Moore String Matching Algorithm  
  
NO_OF_CHARS = 256
  
def badCharHeuristic(string, size): 
    ''' 
    The preprocessing function for 
    Boyer Moore's bad character heuristic 
    '''
  
    # Initialize all occurrence as -1 
    badChar = [-1]*NO_OF_CHARS 
  
    # Fill the actual value of last occurrence 
    for i in range(size): 
        badChar[ord(string[i])] = i; 
  
    # retun initialized list 
    return badChar 
  
def search(txt, pat): 
    ''' 
    A pattern searching function that uses Bad Character 
    Heuristic of Boyer Moore Algorithm 
    '''
    m = len(pat) 
    n = len(txt) 
  
    # create the bad character list by calling  
    # the preprocessing function badCharHeuristic() 
    # for given pattern 
    badChar = badCharHeuristic(pat, m)  
  
    # s is shift of the pattern with respect to text 
    s = 0
    while(s <= n-m): 
        j = m-1
  
        # Keep reducing index j of pattern while  
        # characters of pattern and text are matching 
        # at this shift s 
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
  
        # If the pattern is present at current shift,  
        # then index j will become -1 after the above loop 
        if j<0: 
            print("Pattern occur at shift = {}".format(s)) 
  
            '''     
                Shift the pattern so that the next character in text 
                      aligns with the last occurrence of it in pattern. 
                The condition s+m < n is necessary for the case when 
                   pattern occurs at the end of text 
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1) 
        else: 
            ''' 
               Shift the pattern so that the bad character in text 
               aligns with the last occurrence of it in pattern. The 
               max function is used to make sure that we get a positive 
               shift. We may get a negative shift if the last occurrence 
               of bad character in pattern is on the right side of the 
               current character. 
            '''
            s += max(1, j-badChar[ord(txt[s+j])]) 
  
  
# Driver program to test above function 
def main(): 
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat) 

if __name__ == '__main__': 
    main() 
  
# This code is contributed by Atul Kumar 
# (www.facebook.com/atul.kr.007) 

"""
Output:
 pattern occurs at shift = 4
The Bad Character Heuristic may take O(mn) time in worst case. The worst case occurs when all characters of the text and pattern are same. 
For example, txt[] = “AAAAAAAAAAAAAAAAAA” and pat[] = “AAAAA”.
"""