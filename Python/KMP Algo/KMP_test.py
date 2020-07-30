def lps_array_construction(pattern):
    previous_max_length = 0
    lps_array_length = len(pattern)
    lps_array = [0]*lps_array_length
    i = 1
    while i< lps_array_length:
        if pattern[i] == pattern[previous_max_length]:
            #There's a match, extend i 
            previous_max_length+=1
            lps_array[i] = previous_max_length
            i+=1
        else:
            #If there isn't a match, and there's still more length, go back to check
            if previous_max_length != 0:
                previous_max_length = lps_array[previous_max_length-1]
            
            else:
                #if no previous length and not a current match, 
                lps_array[i]=0
                i+=1
    return lps_array

def KMP(pattern,text):
    pattern_length = len(pattern)
    

