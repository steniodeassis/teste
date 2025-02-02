### Adapted code as in strobogrammatic-iterative.py and 
### strobogrammatic-recursive.py, but return the number of steps

def strobogrammatic_iterative_steps(n):
    '''
    Return all the strobogrammatic numbers that are of length n through iterative
    approach
    ------------
    Parameters:
    n: int
        The targeted length of the digit 
    ------------
    Returns: int
        Number of steps to run the function
    '''
    from itertools import product # 'product' calculates the Cartesian product of n elements out of n sets
    step_counter = 1 # for the two following if statements
    if n <= 0:
        return step_counter
    if n == 1:
        step_counter += 2
        return step_counter
  
    # when n >= 2
    result = []
    number = [0 for i in range(n)]
    step_counter += 2
    for j, k in zip([1, 8, 6, 9], [1, 8, 9, 6]):
        number[0], number[-1] = j, k # define the extreme digits
        step_counter += 5
        if n%2 == 1: # if n is odd
            # calculates the Cartesian product of n//2-1 elements out of n//2-1 sets, resulting in n//2-1 ordered combinations of (1, 0, 6, 8, 9)
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i # add the Cartesian product to the first half of digits between the first and the median
                step_counter += 2
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
                    step_counter += 11
                # adds the median digit because n is odd
                for L in [0, 1, 8]: 
                    number[n//2] = L
                    result.append(''.join(str(e) for e in number))
                    step_counter += 3
                      
        else: # if n is even
            step_counter += 1
            # calculates the Cartesian product of n//2-1 elements out of n//2-1 sets
            for i in product([1, 0, 6, 8, 9], repeat=n//2-1):
                number[1:n//2] = i # add the Cartesian product to the first half of digits between the first until the first middle digit (inclusive)
                step_counter += 2
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
                    step_counter += 11
                result.append(''.join(str(e) for e in number))
                step_counter += 1
    
    result.sort() # sort the result list in ascending order
    step_counter += 1
    
    return step_counter
        

    
def strobogrammatic_recursive_steps(n):
    '''
    Return all the strobogrammatic numbers that are of length n through recursive approach
    ------------
    Parameters:
    n: int
        The targeted length of the digit 
    ------------
    Returns: int
        Number of steps to run the function
    '''
    step_counter = 0
    # Middle generator function
    def middle_generator(N, step_counter=step_counter):  
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
            step_counter += 2
        # base case: when n is odd
        if N == 1:  
            step_counter += 3
            return ["0", "1", "8"]
        # base case: when n is even
        step_counter += 4 # for the previous if statements and the nums definition
        if N == 2:
            nums = [] # list of strobogrammatic numbers of 2 digits
            for j, k in zip([0, 1, 8, 6, 9], [0, 1, 8, 9, 6]): # iterate simultaneously the two lists
                num = [0,0] # each number will treated as a list of digits
                num[0], num[-1] = j, k
                nums.append(''.join(str(e) for e in num)) # convert the number-list to string and add to the major list nums
                step_counter += 5
            step_counter += 1
            return nums
        # when N >= 3
        step_counter += 5 # for the previous if statements and numbers and num definition
        numbers = []
        num = [0 for i in range(N)] # each number will be treated as list of its digits
        for j, k in zip([0, 1, 8, 6, 9], [0, 1, 8, 9, 6]): # create each extreme possibility 
            num[0], num[-1] = j, k # define the extreme digits
            step_counter += 3
            # recursion: the number of digits - 2 (number of digits between the extremes) will be input to the middle_generator() and each output will be added to the middle of the initial number 
            for middle in middle_generator(N-2):
                num[1:-1] = middle
                numbers.append(''.join(str(e) for e in num)) # convert each number-list to string and add to the major list nums
                step_counter += 3
        step_counter += 1
        return numbers
    
    # End of the Middle Generator function
    if n <= 0:
        step_counter += 1
        return step_counter
    if n == 1:
        step_counter += 2
        return step_counter
    
    step_counter += 4 # previous if statements and result and number definition
    # n >= 2
    result = []
    number = [0 for i in range(n)]
    for j, k in zip([1, 8, 6, 9], [1, 8, 9, 6]): 
        number[0], number[-1] = j, k # define the extreme with exception of 0
        step_counter += 3
        for i in middle_generator(n-2): # call the generator and add the middle digits
            number[1:-1] = i
            result.append(''.join(str(e) for e in number))
            step_counter += 2
            
    result.sort() # sort the result list in ascending order
    step_counter += 1
    
    return step_counter


print("Iterative step counter:\n\tN: 5 | steps: ", strobogrammatic_iterative_steps(5))
print("Iterative step counter:\n\tN: 10 | steps: ", strobogrammatic_iterative_steps(10))
print("Iteratve step counter:\n\tN: 15 | steps: ", strobogrammatic_iterative_steps(15))
print("\nRecursive step counter:\n\tN: 5 | steps: ", strobogrammatic_recursive_steps(5))
print("Recursive step counter:\n\tN: 10 | steps: ", strobogrammatic_recursive_steps(10))
print("Recursive step counter:\n\tN: 15 | steps: ", strobogrammatic_recursive_steps(15))

### Adapted from Minerva University CS110 Session 4 - [2.2] 
### Calculate the average running time and the number of steps according to the input value

import time 
import matplotlib.pyplot as plt

max_input = 10
n_list = list(range(1, max_input))
experiments = 50

# Running time Iterative
avg_runtime_iterative = []
for input_ in n_list:
    runtime = []
    for i in range(experiments):
        start_timer = time.process_time()
        strobogrammatic_iterative(input_)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_iterative.append(sum(runtime)/len(runtime))
    
# Running time Recursive
avg_runtime_recursive = []
for input_ in n_list:
    runtime = []
    for i in range(experiments):
        start_timer = time.process_time()
        strobogrammatic_recursive(input_)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_recursive.append(sum(runtime)/len(runtime))
    
# Number of steps Iterative and Recursive
number_steps_iterative = []
number_steps_recursive = []
for input_ in n_list:
    number_steps_iterative.append(strobogrammatic_iterative_steps(input_))
    number_steps_recursive.append(strobogrammatic_recursive_steps(input_))

# PLOT FOR RUN TIME
fig, ax = plt.subplots()
# For running time
ax.plot(n_list, avg_runtime_iterative, color='red', marker='o', label='Iterative')
ax.plot(n_list, avg_runtime_recursive, color='blue', marker='o', label='Recursive')
plt.legend(loc='upper left')
plt.ylabel('Average running time (seconds)')
plt.xlabel('Input')
plt.title('Runtime for Recursive and Iterative functions')

# Plot
plt.show()

# PLOT FOR NUMBER OF STEPS
fig, ax = plt.subplots()
# For Number of steps
ax.plot(n_list, number_steps_iterative, color='red', marker='o', label='Iterative')
ax.plot(n_list, number_steps_recursive, color='blue', marker='o', label='Recursive')
plt.legend(loc='upper left')
plt.ylabel('Number of steps')
plt.xlabel('Input')
plt.title('Numbers of steps for Recursive and Iterative functions\n')

# Plot
plt.show()
