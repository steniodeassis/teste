def recursive_binary_search_extension(nums, target):
    '''
    Return the start and end index (inclusively)
    of a target element in a sorted array
    ------------
    Parameters:
    nums: list
        a sorted array
    target: int
        the target value to be found
    ------------
    Returns:
    list/ None
        list of the beginning and end index if found, else None
    '''
    result = [] # final result 
    tracker = [] # track the matches' indexes
    
    # track_counter function applies the recursive track and 
    def track_counter(new_nums, new_target, i=0, j=0):
        
        # i iterate between the indices of new_nums
        # tracker store the position of the matches 
        if i == len(new_nums): #base case
            
            if j != 0: # j counts the number of matches
                # end of iteration any match, return result
                # add in result the position of the first match, last match and number of matches
                result.append(tracker[0])
                result.append(tracker[-1])
                result.append(j)
                return result
 
        else: # calls the recursion
            #if a match is found add its index i to the tracker list
            # and increase j by one
            if new_nums[i] == new_target:
                tracker.append(i)
                j += 1
            # call the function again for new values of i and j     
            track_counter(new_nums, new_target, i+1, j)
    
    track_counter(nums, target)
    if len(result) != 0:
        return result
    else:
        return None

# assert for the recursive approach
assert(recursive_binary_search_extension([1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 2) == [2, 5, 4])
assert(recursive_binary_search_extension([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 1) == [0, 5, 6])
assert(recursive_binary_search_extension([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 0) == None)
