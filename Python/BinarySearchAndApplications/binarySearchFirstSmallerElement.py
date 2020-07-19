"""
Note that on each iteration we drop off at least half the remaining elements from consideration. If the top branch executes, then the elements 
in the range [low, (low + high) / 2] are all discarded, causing us to lose floor((low + high) / 2) – low + 1 >= (low + high) / 2 – low = (high – low) / 2 elements.

If the bottom branch executes, then the elements in the range [(low + high) / 2 + 1, high] are all discarded. This loses us 
high – floor(low + high) / 2 + 1 >= high – (low + high) / 2 = (high – low) / 2 elements.

Consequently, we’ll end up finding the first element smaller than the target in O(lg n) iterations of this process.
"""

# Python3 program to find first element that  
# is strictly smaller than given target 
    
def next(arr, target):  
  
    start = 0;  
    end = len(arr) - 1;  
    
    ans = -1;  
    while (start <= end):  
        mid = (start + end) // 2;  
    
        # Move to the left side if target is  
        # smaller  
        if (arr[mid] >= target):  
            end = mid - 1;  
    
        # Move right side  
        else:  
            ans = mid;  
            start = mid + 1;  
    
    return ans;  
    
# Driver code  
if __name__ == '__main__':  
  
    arr = [ 1, 2, 3, 5, 8, 12 ];  
    print(next(arr, 5));  
    
# This code is contributed by Yash_R