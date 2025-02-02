## Insertion sort until array size k, then merge.

def insertion_sort_until_k(arr, start, end, k = 10):
    '''
    Sort the input array in ascending order using insertion sort until the array size is k, which shift to merge sort
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
    arr : list
        Ordered input array in ascending order
    '''
    # if array size is less than k, apply merge sort directly
    if len(arr) < k:
        merge_sort(arr, start, end)
    
    # otherwise it will apply insertion sort until the first end-k elements, and the remaining will be sorted by merge sort
    else:
        # insertion sort for in between the first element and the end-k element
        for j in range(start+1, end-k+1):
            # if j < end-k+1:
            key = arr[j]
            i = j-1
            # insert the key when the key is bigger than the previous number
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]
                i -= 1
            arr[i+1] = key
        # after insertion sort, apply merge sort to the last elements (end-k and end).
        merge_sort(arr, end-k+1, end)
        # merge the entire list
        merge_sort(arr, start, end)
    
    return arr


def merge(A, p, q, r):
    '''
    Merge the input array in ascending order
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
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+= 1
            
def merge_sort(arr, start, end):
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
    Return:
    -----
    arr : list
        Ordered input array in ascending order
    '''
    if start < end:
        m = start+(end-start)//2
        
        merge_sort(arr, start, m)
        merge_sort(arr, m+1, end)
        merge(arr, start, m, end)

## Test cases
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]
assert(insertion_sort_until_k(A, 0, len(A)-1) == sorted(A))

B = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
assert(insertion_sort_until_k(B, 0, len(B)-1) == sorted(B))

C = [5, 4, 3, 2, 1]
assert(insertion_sort_until_k(C, 0, len(C)-1) == sorted(C))
