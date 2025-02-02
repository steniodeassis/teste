def iterative_binary_search_extension(nums, target):
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
        list of the beginning index, end index and total number of indexes
        if found, else None
    '''
    counter = 0 # track the number of matches
    result = [] # track the result 
    tracker = [] # track the position of the matches
    
    # iterate over nums by indexing
    for i in range(0, len(nums)):
        # if a match, add the match into tracker and increase counter by one
        if nums[i] == target:
            tracker.append(i)
            counter += 1
    # if there was no match return None
    if counter == 0:
        return None
    # otherwise append the first and last position match with the number of matches into result and return it
    else:
        result.append(tracker[0])
        result.append(tracker[-1])
        result.append(counter)
        return result

# assert of the iterative approach
assert(iterative_binary_search_extension([1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 2) == [2, 5, 4])
assert(iterative_binary_search_extension([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 1) == [0, 5, 6])
assert(iterative_binary_search_extension([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 0) == None)
