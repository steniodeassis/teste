## ITERATIVE
def strobogrammatic_iterative(n):
    from itertools import product # product calculates the Cartesian product of n elements out of n sets
    
    if n <= 0:
        raise ValueError("Input should be greater than zero")

    if n == 1:
        return ['0', '1', '8']
    
    result = []
    number = [0 for i in range(n)]
    for j, k in zip([1, 8, 6, 9], [1, 8, 9, 6]):
        number[0] = j
        number[-1] = k
        if n%2 == 1: # if the digits' number is odd
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i
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
                        
                for L in [0, 1, 8]: # adds the inner number
                    number[n//2] = L
                    result.append(''.join(str(e) for e in number))
                    
        else: # if digits' number is even 
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i
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

print(strobogrammatic_iterative(5))
