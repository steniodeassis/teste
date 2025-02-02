## Merge sort until array sized k, then insertion sort.

def merge(A, p, q, r):
    '''
    Merge the entire list back
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
    A : list
        The initial list ordered in ascending order
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
            i += 1
        else:
            A[k] = R[j]
            j += 1

def insertion_sort(arr):
    '''
    Sort the input array in ascending order
    Parameters:
    -----
    arr : list
        Unordered input array
    Return:
    -----
    arr : list
        Ordered input array in ascending order
    '''
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        # insert the key when the key is bigger than the previous number
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    
    return arr
    
def merge_sort_until_k(arr, start, end, k = 10):
    '''
    Sort the input array in ascending order
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
    Return:
    -----
    arr : list
        Ordered input array in ascending order
    '''
    if end-start < k:
        # it sorts the half of arr by insertion
        arr[start:end+1] = insertion_sort(arr[start:end+1])
        
    # if end-start > k, call merge sort
    else:
        m = start+(end-start)//2
        # divide the list in two
        merge_sort_until_k(arr, start, m)
        merge_sort_until_k(arr, m+1, end)
        # call merge to combine the list back
        merge(arr, start, m, end)
        
    return arr

### test cases
A = [0, 1, 0, 1, 0, 1, 0, -1, 2, 5, 2, 1, 0, 1, 0, 1, 0, 1, 0]
assert(merge_sort_until_k(A, 0, len(A)-1) == sorted(A))

B = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]
assert(merge_sort_until_k(B, 0, len(B)-1) == sorted(B))

C = [1, 2, 2, 2, 2, 2, 2, -1, -2, -3, -4, -5, 0]
assert(merge_sort_until_k(C, 0, len(C)-1) == sorted(C))


