# RECURSIVE
def strobogrammatic_recursive(n):
    '''
    Return all the strobogrammatic numbers that are of length n through recursive approach
    ------------
    Parameters:
    n: int
        The targeted length of the digit 
    ------------
    Returns: list
        All strobogrammatic numbers that are of the targeted length
    '''
    # Middle generator function
    def middle_generator(N):  
        '''
        Generate the strobogrammatic numbers that are of length n-2 through recursive approach
        It will be used for the inner digits (not-extremes)
        ------------
        Parameters:
        N: int
            The targeted length of the digit 
        ------------
        Returns: list
             All strobogrammatic numbers that are of the targeted length
        '''
        if N == 0:
            return [""]
        # base case: when n is odd
        if N == 1:  
            return ["0", "1", "8"]
        # base case: when n is even
        if N == 2:
            nums = [] # list of strobogrammatic numbers of 2 digits
            for j, k in zip([0, 1, 8, 6, 9], [0, 1, 8, 9, 6]): # iterate simultaneously the two lists
                num = [0,0] # each number will treated as a list of digits
                num[0], num[-1] = j, k
                nums.append(''.join(str(e) for e in num)) # convert the number-list to string and add to the major list nums
            return nums
        # when N >= 3
        numbers = []
        num = [0 for i in range(N)] # each number will be treated as list of its digits
        for j, k in zip([0, 1, 8, 6, 9], [0, 1, 8, 9, 6]): # create each extreme possibility 
            num[0], num[-1] = j, k # define the extreme digits
            # recursion: the number of digits - 2 (number of digits between the extremes) will be input to the middle_generator() and each output will be added to the middle of the initial number 
            for middle in middle_generator(N-2):
                num[1:-1] = middle
                numbers.append(''.join(str(e) for e in num)) # convert each number-list to string and add to the major list nums
        return numbers
    
    # End of the Middle Generator function
    
    if n <= 0:
        raise ValueError("Input should be greater than zero")
    if n == 1:
        return ['0', '1', '8']
    
    # n >= 2
    result = []
    number = [0 for i in range(n)]
    for j, k in zip([1, 8, 6, 9], [1, 8, 9, 6]): 
        number[0], number[-1] = j, k # define the extreme with exception of 0
        for i in middle_generator(n-2): # call the generator and add the middle digits
            number[1:-1] = i
            result.append(''.join(str(e) for e in number))
    
    result.sort() # sort the result list in ascending order
    
    return result

# Assert test for strobogrammatic recursive
assert(strobogrammatic_recursive(1) == ["0", "1", "8"])
assert(strobogrammatic_recursive(2) == ['11', '69', '88', '96'])
assert(strobogrammatic_recursive(3) == ['101', '111', '181', '609', '619', '689', '808', '818', '888', '906', '916', '986'])
