
"""
Note that on each iteration we drop off at least half the remaining elements from consideration. If the top branch executes, then the elements in the 
range [low, (low + high) / 2] are all discarded, causing us to lose floor((low + high) / 2) – low + 1 >= (low + high) / 2 – low = (high – low) / 2 elements.

If the bottom branch executes, then the elements in the range [(low + high) / 2 + 1, high] are all discarded. This loses us 
high – floor(low + high) / 2 + 1 >= high – (low + high) / 2 = (high – low) / 2 elements.

Consequently, we’ll end up finding the first element greater than the target in O(lg n) iterations of this process.
"""



# Python program to find first element that 
# is strictly greater than given target. 
  
def next(arr, target): 
    start = 0; 
    end = len(arr) - 1; 
  
    ans = -1; 
    while (start <= end): 
        mid = (start + end) // 2; 
  
        # Move to right side if target is 
        # greater. 
        if (arr[mid] <= target): 
            start = mid + 1; 
  
        # Move left side. 
        else: 
            ans = mid; 
            end = mid - 1; 
  
    return ans; 
  
# Driver code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 5, 8, 12]; 
    print(next(arr, 8)); 
  
# This code is contributed by 29AjayKumar 
