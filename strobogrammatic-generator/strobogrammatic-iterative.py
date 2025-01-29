## ITERATIVE
def strobogrammatic_iterative(n):
    '''
    Return all the strobogrammatic numbers that are of length n through iterative
    approach
    ------------
    Parameters:
    n: int
        The targeted length of the digit 
    ------------
    Returns: list
        All strobogrammatic numbers that are of the targeted length
    '''
    from itertools import product # 'product' calculates the Cartesian product of n elements out of n sets
    
    if n <= 0:
        raise ValueError("Input should be greater than zero")
    if n == 1:
        return ['0', '1', '8']
  
    # when n >= 2
    result = []
    number = [0 for i in range(n)]
    for j, k in zip([1, 8, 6, 9], [1, 8, 9, 6]):
        number[0], number[-1] = j, k # define the extreme digits
        if n%2 == 1: # if n is odd
            # calculates the Cartesian product of n//2-1 elements out of n//2-1 sets, resulting in n//2-1 ordered combinations of (1, 0, 6, 8, 9)
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i # add the Cartesian product to the first half of digits between the first and the median
                # mirror the Cartersian product to create strobogrammatic numbers
                for p in range(1, n//2):
                    if number[p] == 6:
                        number[-p-1] = 9
                    elif number[p] == 9:
                        number[-p-1] = 6
                    elif number[p] == 8:
                        number[-p-1] = 8
                    elif number[p] == 1:
                        number[-p-1] = 1
                    elif number[p] == 0:
                        number[-p-1] = 0
                # adds the median digit because n is odd
                for L in [0, 1, 8]: 
                    number[n//2] = L
                    result.append(''.join(str(e) for e in number))
                    
        else: # if n is even 
            # calculates the Cartesian product of n//2-1 elements out of n//2-1 sets
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i # add the Cartesian product to the first half of digits between the first until the first middle digit (inclusive)
                # mirror the Cartersian product
                for p in range(1, n//2):
                    if number[p] == 6:
                        number[-p-1] = 9
                    elif number[p] == 9:
                        number[-p-1] = 6
                    elif number[p] == 8:
                        number[-p-1] = 8
                    elif number[p] == 1:
                        number[-p-1] = 1
                    elif number[p] == 0:
                        number[-p-1] = 0
                result.append(''.join(str(e) for e in number))
    
    result.sort() # sort the result list in ascending order
    
    return result
    
# Assert test for strobogrammatic iterative
assert(strobogrammatic_iterative(1) == ["0", "1", "8"])
assert(strobogrammatic_iterative(2) == ['11', '69', '88', '96'])
assert(strobogrammatic_iterative(3) == ['101', '111', '181', '609', '619', '689', '808', '818', '888', '906', '916', '986'])
