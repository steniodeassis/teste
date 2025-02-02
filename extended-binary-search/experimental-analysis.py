### NUMBER OF STEPS
def iterative_binary_search_extension_steps(nums, target):
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
    step_counter: int
        The number of steps
    '''
    step_counter = 0 # define the step counter
    counter = 0 # track the number of matches
    result = [] # track the result 
    tracker = [] # track the position of the matches
    
    # iterate over nums by indexing
    for i in range(0, len(nums)):
        step_counter += 1
        # if a match, add the match into tracker and increase counter by one
        if nums[i] == target:
            tracker.append(i)
            counter += 1
            step_counter += 3
    # if there was no match return None
    if counter == 0:
        step_counter += 2
        return step_counter
    # otherwise append the first and last position match with the number of matches into result and return it
    else:
        step_counter += 4
        result.append(tracker[0])
        result.append(tracker[-1])
        result.append(counter)
        return step_counter

def recursive_binary_search_extension_steps(nums, target):
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
    step_counter: int
        The number of steps
    '''
    step_counter = [] # define the step counter
    result = [] # final result 
    tracker = [] # track the matches' indexes
    
    # track_counter function applies the recursive track and 
    def track_counter(new_nums, new_target, i=0, j=0):
        
        # i iterate between the indices of new_nums
        # tracker store the position of the matches 
        if i == len(new_nums): #base case
            step_counter.append(1)
            if j != 0: # j counts the number of matches
                # end of iteration any match, return result
                # add in result the position of the first match, last match and number of matches
                step_counter.append(4)
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
                step_counter.append(4)
            # call the function again for new values of i and j     
            step_counter.append(1)
            track_counter(new_nums, new_target, i+1, j)
    
    step_counter.append(4)
    track_counter(nums, target)
    steps = sum(step_counter)
    if len(result) != 0:
        return steps
    else:
        return steps


# Assert test for iterative_binary_search_extension_steps()
assert(iterative_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15], 12) == 26)
assert(iterative_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15], 15) == 41)
assert(iterative_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15], 14) == 26)

# Assert test using the same inputs for recursive_binary_search_extension_steps()
assert(recursive_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15], 12) == 35)
assert(recursive_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15], 15) == 53)
assert(recursive_binary_search_extension_steps([11, 11, 12, 12, 12, 12, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15], 14) == 33)


## RUNNING TIME
### adaptated from CS110 Session 4 - [2.2]
### Calculate the average running time and the number of steps to the input value for the postal code
### and plot the results

import time 
import matplotlib.pyplot as plt
import random

max_array_ele = 100 # define the last element in the array and also the size of the last array
min_array_ele = 0

number_array_ele = [i for i in range(min_array_ele, max_array_ele)] # a list between the first and last element in an array
list_arrays = []
list_targets = []

experiments = 100 # number of experiments to be done

# Compute array samples from size min_array_ele until max_array_ele
for array_size in range(min_array_ele, max_array_ele):
    pool_list = [i for i in range(min_array_ele, max_array_ele)]
    postal_array_sample = random.choices(pool_list, k=array_size) # create a sample array

    postal_array_sample.sort()
    list_arrays.append(postal_array_sample)
    
    target_ele = random.randint(0, 100) # create a sample target
    list_targets.append(target_ele)
    

# Running time for iterative_binary_search_extension
avg_runtime_iterative = []
for array, target in zip(list_arrays, list_targets):
    runtime = []
    for i in range(experiments):
        start_timer = time.process_time()
        iterative_binary_search_extension(array, target)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_iterative.append(sum(runtime)/len(runtime))
    
# Running time for recursive_binary_search_extension
avg_runtime_recursive = []
for array, target in zip(list_arrays, list_targets):
    runtime = []
    for i in range(experiments):
        start_timer = time.process_time()
        recursive_binary_search_extension(array, target)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_recursive.append(sum(runtime)/len(runtime))
    
# Number of steps Iterative and Recursive
number_steps_iterative = []
number_steps_recursive = []
for array, target in zip(list_arrays, list_targets):
    number_steps_iterative.append(iterative_binary_search_extension_steps(array, target))
    number_steps_recursive.append(recursive_binary_search_extension_steps(array, target))

# Plot the combined graphics
fig, ax = plt.subplots()
# For running time
ax.plot(number_array_ele, avg_runtime_iterative, color='red', label='Iterative')
ax.plot(number_array_ele, avg_runtime_recursive, color='blue', label='Recursive')
plt.legend(loc='upper left')
plt.ylabel('Average running time (seconds)')
plt.xlabel('Input array size')
plt.title('Runtime for Recursive and Iterative functions')

# Plot
plt.show()

