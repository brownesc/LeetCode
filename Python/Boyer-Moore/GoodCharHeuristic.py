# Good Suffix Heuristic

# Let t be substring of text T which is matched with substring of pattern P. Now we shift pattern until :
# 1) Another occurrence of t in P matched with t in T.
# 2) A prefix of P, which matches with suffix of t
# 3) P moves past t

# Case 1: Another occurrence of t in P matched with t in T
# Pattern P might contain few more occurrences of t. In such case, we will try to shift the pattern to align that occurrence with t in text T.

# Case 2: A prefix of P, which matches with suffix of t in T
# It is not always likely that we will find the occurrence of t in P. Sometimes there is no occurrence at all, in such cases sometimes we can 
# search for some suffix of t matching with some prefix of P and try to align them by shifting P. 

# Case 3: P moves past t

"""
Preprocessing for Good suffix heuristic

As a part of preprocessing, an array shift is created. Each entry shift[i] contain the distance pattern will shift if mismatch occur at position i-1. 
That is, the suffix of pattern starting at position i is matched and a mismatch occur at position i-1. Preprocessing is done separately for strong 
good suffix and case 2 discussed above.

1) Preprocessing for Strong Good Suffix
Before discussing preprocessing, let us first discuss the idea of border. A border is a substring which is both proper suffix and proper 
prefix. For example, in string “ccacc”, “c” is a border, “cc” is a border because it appears in both end of string but “cca” is not a border.

As a part of preprocessing an array bpos (border position) is calculated. Each entry bpos[i] contains the starting index of border for suffix 
starting at index i in given pattern P.The suffix φ beginning at position m has no border, so bpos[m] is set to m+1 where m is the length of the pattern.
The shift position is obtained by the borders which cannot be extended to the left. Following is the code for preprocessing –

void preprocess_strong_suffix(int *shift, int *bpos,
                  char *pat, int m)
{
    int i = m, j = m+1;
    bpos[i] = j;
    while(i > 0)
    {
        while(j <= m && pat[i-1] != pat[j-1])
        {
            if (shift[j] == 0)
                shift[j] = j-i;
            j = bpos[j];
        }
        i--; j--;
        bpos[i] = j; 
    }
}
Explanation: Consider pattern P = “ABBABAB”, m = 7.

The widest border of suffix “AB” beginning at position i = 5 is φ(nothing) starting at position 7 so bpos[5] = 7.
At position i = 2 the suffix is “BABAB”. The widest border for this suffix is “BAB” starting at position 4, so j = bpos[2] = 4.

2) Preprocessing for Case 2
In the preprocessing for case 2, for each suffix the widest border of the whole pattern that is contained in that suffix is determined.

"""

# Python3 program for Boyer Moore Algorithm with  
# Good Suffix heuristic to find pattern in  
# given text string 
  
# preprocessing for strong good suffix rule 
def preprocess_strong_suffix(shift, bpos, pat, m): 
  
    # m is the length of pattern 
    i = m 
    j = m + 1
    bpos[i] = j 
  
    while i > 0: 
          
        '''if character at position i-1 is  
        not equivalent to character at j-1,  
        then continue searching to right  
        of the pattern for border '''
        while j <= m and pat[i - 1] != pat[j - 1]: 
              
            ''' the character preceding the occurrence  
            of t in pattern P is different than the  
            mismatching character in P, we stop skipping 
            the occurrences and shift the pattern  
            from i to j '''
            if shift[j] == 0: 
                shift[j] = j - i 
  
            # Update the position of next border 
            j = bpos[j] 
              
        ''' p[i-1] matched with p[j-1], border is found.  
        store the beginning position of border '''
        i -= 1
        j -= 1
        bpos[i] = j 
  
# Preprocessing for case 2 
def preprocess_case2(shift, bpos, pat, m): 
    j = bpos[0] 
    for i in range(m + 1): 
          
        ''' set the border position of the first character  
        of the pattern to all indices in array shift 
        having shift[i] = 0 '''
        if shift[i] == 0: 
            shift[i] = j 
              
        ''' suffix becomes shorter than bpos[0],  
        use the position of next widest border 
        as value of j '''
        if i == j: 
            j = bpos[j] 
  
'''Search for a pattern in given text using  
Boyer Moore algorithm with Good suffix rule '''
def search(text, pat): 
  
    # s is shift of the pattern with respect to text 
    s = 0
    m = len(pat) 
    n = len(text) 
  
    bpos = [0] * (m + 1) 
  
    # initialize all occurrence of shift to 0 
    shift = [0] * (m + 1) 
  
    # do preprocessing 
    preprocess_strong_suffix(shift, bpos, pat, m) 
    preprocess_case2(shift, bpos, pat, m) 
  
    while s <= n - m: 
        j = m - 1
          
        ''' Keep reducing index j of pattern while characters of  
            pattern and text are matching at this shift s'''
        while j >= 0 and pat[j] == text[s + j]: 
            j -= 1
              
        ''' If the pattern is present at the current shift,  
            then index j will become -1 after the above loop '''
        if j < 0: 
            print("pattern occurs at shift = %d" % s) 
            s += shift[0] 
        else: 
              
            '''pat[i] != pat[s+j] so shift the pattern  
            shift[j+1] times '''
            s += shift[j + 1] 
  
# Driver Code 
if __name__ == "__main__": 
    text = "ABAAAABAACD"
    pat = "ABA"
    search(text, pat) 
  
# This code is contributed by 
# sanjeev2552 

"""
Output:
pattern occurs at shift = 0
pattern occurs at shift = 5
"""