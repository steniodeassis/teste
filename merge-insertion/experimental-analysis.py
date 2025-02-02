## STEP COUNTER
### Step counter for insertion_sort_until_k
def insertion_sort_until_k_steps(arr, start, end, k = 10):
    '''
    Sort the input array in ascending order using insertion sort until the array size is k, which shift to merge sort and return the number of steps the code took to be executed
    Parameters:
    -----
    arr : list
        Unordered input array
    start : int
        The first element index
    end : int
        The last element index
    Return:
    -----
    steps : int
        The number of steps the algorithm takes to run
    '''
    steps = 0 # the step counter 
    # if array size is less than k, apply merge sort directly
    if len(arr) < k:
        steps += 2 # for the if statement and for the merge_sort call
        steps = merge_sort_steps(arr, start, end, steps)
    
    # otherwise it will apply insertion sort until the first end-k elements, and the remaining will be sorted by merge sort
    else:
        steps += 2
        # insertion sort for in between the first element and the end-k element
        for j in range(start+1, end-k+1):
            steps += 3 # for loop and bellow assignments
            # if j < end-k+1:
            key = arr[j]
            i = j-1
            # insert the key when the key is bigger than the previous number
            while i >= 0 and arr[i] > key:
                steps += 3
                arr[i+1] = arr[i]
                i -= 1
            arr[i+1] = key
            steps += 1
        # after insertion sort, apply merge sort to the last elements (end-k and end) and assign the number of steps
        steps = merge_sort_steps(arr, end-k+1, end, steps)
        # merge the entire list and assign the number of steps 
        steps = merge_sort_steps(arr, start, end, steps)
    
    return steps


def merge_steps(A, p, q, r, steps):
    '''
    Merge the input array in ascending order and return the number of steps it took to merge
    Parameters:
    -----
    A : list
        Unordered input array
    p : int
        First element index
    q : int
        Middle element index
    r : int
        Last element index
    steps : int
        The number of steps the code take to run
    Return:
    -----
    A : list
        Ordered input array in ascending order
    '''
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    steps += 6 # for the above assignments
    for k in range(p, r+1):
        steps += 1 # for the for loop
        if L[i] <= R[j]:
            steps += 3
            A[k] = L[i]
            i+=1
        else:
            steps += 4
            A[k] = R[j]
            j += 1
    return steps

def merge_sort_steps(arr, start, end, steps):
    '''
    Sort the input array in ascending order using by calling merge() function recursively
    Parameters:
    -----
    arr : list
        Unordered input array
    start : int
        First element index
    end : int
        Last element index
    steps : int
        The inital number of steps from the insertion_sort_until_k
    Return:
    -----
    steps : int
        The final number of steps the code took to run
    '''
    steps += 1
    if start < end:
        steps += 3 # for the m assignment and the merge_sort calling
        m = start+(end-start)//2
        
        merge_sort_steps(arr, start, m, steps)
        merge_sort_steps(arr, m+1, end, steps)
        steps += 1 # for the bellow merge calling
        steps = merge_steps(arr, start, m, end, steps)
        
    return steps


### Step counter for merge_sort algorithm
def merge_steps(A, p, q, r, steps):
    '''
    Merge the entire list back and return the number of steps it took to executed the code
    Parameters:
    -----
    A : list
        The unordered list
    p : int
        First element index
    q : int
        Middle element index
    r : int
        Last element index
    Return
    ------
    step : list
        The number of steps the code took to run
    '''
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    steps += 6 # for the above assignments
    for k in range(p, r+1):
        steps += 1
        if L[i] <= R[j]:
            steps += 3
            A[k] = L[i]
            i += 1
        else:
            steps += 4
            A[k] = R[j]
            j += 1
            
    return steps

def insertion_sort_steps(arr, steps):
    '''
    Sort the input array in ascending order and return and the number of steps the code took to run
    Parameters:
    -----
    arr : list
        Unordered input array
    Return:
    -----
    arr : list
        The sorted list by insertion
    steps : list
        The number of steps the code took to run
    '''
    for j in range(1, len(arr)):
        steps += 3 # for the for loop and the variable definitions
        key = arr[j]
        i = j-1
        # insert the key when the key is bigger than the previous number
        while i >= 0 and arr[i] > key:
            steps += 3
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        steps += 1
    
    return arr, steps
    
def merge_sort_until_k_steps(arr, start, end, k=10, steps=0):
    '''
    Sort the input array in ascending order and return and number of steps the code took to run
    Parameters:
    -----
    arr : list
        Unordered input array
    start : int
        The first element index
    middle : int
        The middle element index
    end : int
        The last element index
    steps : int
        Count the number of steps during the recursion
    Return:
    -----
    steps : list
        Ordered input array in ascending order
    '''
    if end-start < k:
        steps += 2 # for the if statement and the insertion calling
        # it sorts the half of arr by insertion
        arr[start:end+1], steps = insertion_sort_steps(arr[start:end+1], steps)
    
    else:
        steps += 3 # for the if, elif, m definition and merge_sort calling
        m = start+(end-start)//2
        # divide the list in two
        merge_sort_until_k_steps(arr, start, m, steps=steps)
        merge_sort_until_k_steps(arr, m+1, end, steps=steps)
        # call merge to combine the list back
        steps += 1
        steps = merge_steps(arr, start, m, end, steps)
        
    return steps

# PLOTING
## adaptated from CS110 Session 4 - [2.2]
## TIME ANALYSIS
import random
import time
import matplotlib.pyplot as plt

max_input_size = 200
n_list = list(range(1, max_input_size))
experiments = 50
k = 5

# merge_sort_until_k time analysis
avg_runtime_merge = []
for input_size in n_list:
    runtime = []
    arr = [random.randrange(-1000, 1000) for _ in range(input_size)]
    #k = len(arr) # for k equal to n
    for _ in range(experiments):
        start_timer = time.process_time()
        merge_sort_until_k(arr, 0, len(arr)-1, k)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_merge.append(sum(runtime)/len(runtime))
    
# insertion_sort_until_k time analysis
avg_runtime_insertion = []
for input_size in n_list:
    runtime = []
    arr = [random.randrange(-1000, 1000) for _ in range(input_size)]
    #k = len(arr) # for k equal to n
    for _ in range(experiments):
        start_timer = time.process_time()
        insertion_sort_until_k(arr, 0, len(arr)-1, k)
        runtime.append(time.process_time()-start_timer)
    avg_runtime_insertion.append(sum(runtime)/len(runtime))
    
#plotting
fig, ax = plt.subplots()
ax.plot(n_list, avg_runtime_merge, color='blue', label='merge_sort_until_k')
ax.plot(n_list, avg_runtime_insertion, color='green', label='insertion_sort_until_k')
plt.legend(loc='upper left')
plt.title('Average runtime of merge_sort_until_k and insertion_sort_until_k for k={}\n'.format(k))
plt.xlabel('Input size')
plt.ylabel('Average runtime (seconds)')
plt.show()

### STEPS ANALYSIS
import random
import matplotlib.pyplot as plt

max_input_size = 500
n_list = list(range(1, max_input_size))
k = 5

# Number of steps for merge_sort_until_k and insertion_sort_until_k
number_steps_merge = []
number_steps_insertion = []
for input_size in n_list:
    arr = [random.randrange(-1000, 1000) for _ in range(input_size)]
    #k = len(arr) # for k equal to n
    # for merge_sort_until_k
    number_steps_merge.append(merge_sort_until_k_steps(arr, 0, len(arr)-1, k))
    # for insertion_sort_until_k
    number_steps_insertion.append(insertion_sort_until_k_steps(arr, 0, len(arr)-1, k))
    
# plotting
fig, ax = plt.subplots()
ax.plot(n_list, number_steps_merge, color='blue', label='merge_sort_until_k_steps')
ax.plot(n_list, number_steps_insertion, color='green', label='insertion_sort_until_k_steps')
plt.legend(loc='upper left')
plt.title('Number of steps for merge_sort_until_k and insertion_sort_until_k when k={}\n'.format(k))
plt.xlabel('Input size')
plt.ylabel('Number of steps')
plt.show()
