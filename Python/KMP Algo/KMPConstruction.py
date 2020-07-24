def KMPSearch(pat, txt): 
    length_of_pattern = len(pat)
    length_of_text = len(txt)

    #Create array for preprocessing
    longest_proper_prefix_also_suffix = [0]*length_of_pattern

    text_index = 0
    pattern_index = 0

    while text_index < length_of_text: 
        if pat[pattern_index] == txt[text_index]: 
            text_index += 1
            pattern_index += 1
  
        if pattern_index == length_of_pattern: 
            print("Found pattern at index " + str(text_index-pattern_index))
            pattern_index = longest_proper_prefix_also_suffix[pattern_index-1] 
  
        # mismatch after pattern_index matches 
        elif text_index < length_of_text and pat[pattern_index] != txt[text_index]: 
            # Do not match lps[0..lps[pattern_index-1]] characters, 
            # they will match anyway 
            if pattern_index != 0: 
                pattern_index = longest_proper_prefix_also_suffix[pattern_index-1] 
            else: 
                text_index += 1

def computeLPSArray(pattern,length_of_pattern,longest_proper_prefix_also_suffix):
    maximum_previous_prefix_suffix_length = 0

    longest_proper_prefix_also_suffix[0] # lps[0] is always 0 
    index = 1
  
    # the loop calculates lps[i] for index = 1 to length_of_pattern -1 
    while index < length_of_pattern: 
        print("index =",index)
        print("maximum_previous_prefix_suffix_length =", maximum_previous_prefix_suffix_length)
        if pattern[index]== pattern[maximum_previous_prefix_suffix_length]:
            print("pattern["+str(index)+"] == patern["+str(maximum_previous_prefix_suffix_length)+"]") 
            maximum_previous_prefix_suffix_length += 1
            print("maximum_previous_prefix_suffix_length =", maximum_previous_prefix_suffix_length)
            longest_proper_prefix_also_suffix[index] = maximum_previous_prefix_suffix_length
            print("longest_proper_prefix_also_suffix["+str(index)+"] ="+str(maximum_previous_prefix_suffix_length))
            index += 1
            print("updated index =",index)
            print(longest_proper_prefix_also_suffix)
            
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and index = 7. The idea is similar  
            # to search step. 
            if maximum_previous_prefix_suffix_length != 0: 
                print('maximum_previous_prefix_suffix_length!=0 so')
                maximum_previous_prefix_suffix_length = longest_proper_prefix_also_suffix[maximum_previous_prefix_suffix_length-1] 
                print(maximum_previous_prefix_suffix_length)
                print(longest_proper_prefix_also_suffix)
                # Also, note that we do not increment index here 
            else: 
                print("else_branch, update array")
                longest_proper_prefix_also_suffix[index] = 0
                index += 1
                print(longest_proper_prefix_also_suffix)
                print("index =",index)

    print("finally, we have")
    print(longest_proper_prefix_also_suffix)
