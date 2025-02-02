# Data Structures and Algorithms (DSA)
The following is a series of codes using iterative and recursive approaches to solve DSA problems, alongside the experimental analysis for each algorithm.

## **Strobogrammatic Number Generator**
A strobogrammatic number is a number that looks the same when rotated upside down, such as 8, 101, 96. Here we consider 1 to be strobogrammatic.
I developed two codes using a **iterative** and **recursive** approach that takes an integer _n_ as input and returns all the strobogrammatic numbers of length _n_ in a list.

### Iterative Approach

In the iterative approach, if the number of digits is 1, the strobogrammatic number can be either 0, 1, or 8. 

For digits greater than 2, we first define the extreme values as 1-1, 8-8, 6-9, or 9-6 (it cannot be 0 since the digit number would be less than expected). Then, for each empty place in the first half of the digits, between the left-extreme and the median (if the digit number is odd), we calculate the Cartesian product. Cartesian product of two sets $A \times B$ is the set of all the ordered pairs $(a, b)$ such that $a$ belongs to $A$ and $b$ belongs to $B$. This approach would extend the number of Cartesian product factors (or initial sets $A \times B \times C \times \dots$) to the number of places between the left-extreme and the median (both exclusive), where its elements could only assume values of (0, 1, 8, 6, 9). We would assign each combination generated $(a, b, c, \dots)$ as a strobogrammatic for each extreme-values combination. The second half of digits, after the median and before the right-extreme, would be defined as the mirrored value of its complementary. 

If the digit number is odd, a center value will be added for each combination generated. This value would assume either 0, 1, or 8. If the digit number is even, such a center value would not exist, and the code would be done, outputting all numbers.

### Recursive Approach

If the length of a strobogrammatic number is 1, there are only three possible possibilities. The number can be 0, 1, or 8. However, when the number of digits is greater than 1, the number can be composed of 6 and 9 (and vice-versa) when they are equidistant concerning the median digit.

A better way to create such numbers from a recursive approach is by defining a sub-function that can be called for when the input size is bigger than 1. This function should define the extremities of the numbers to be either (1-1, 8-8, 6-9, or 9-6). These extremes would be disregarded for the recursion input, and then the subfunction would be called to return for the inner values for the new extremities. However, the values would now consider the equidistant pair 0-0. Therefore, its values would assume the (0-0, 1-1, 8-8, 6-9, 9-6) pairs. The code ends when the function reaches the base case: the center values, which can be either (0, 1, 8) if the input size is odd, or (00, 11, 88, 69, 96) when it is even.

### Flowchart
![strobogrammatic() (1)](https://github.com/user-attachments/assets/d91b051b-54c7-41c9-bfdf-ee3d25b8eb33)
![strobogrammatic() (2)](https://github.com/user-attachments/assets/245a2443-aadd-4920-bf51-52462641de97)


### Experimental Analysis
I designed experiments to determine the average run time and number of steps that both implementations take for increasing values of $n$ [here](/strobogrammatic-generator/experimental-analysis.py).

**Iterative step counter:**

N: 5 | steps:  464

N: 10 | steps:  117528

N: 15 | steps:  4812524

**Recursive step counter:**

N: 5 | steps:  137

N: 10 | steps:  5017

N: 15 | steps:  375017

From the two plots below, there is a divergence of efficiency between the number of steps and the running time for both algorithms. The iterative function increases its number of steps more than the recursive function for increased input values. This is surprising, given the recursive approach was supposed to call for more steps as the function grows. This might be caused by the itertools.product() function that is called inside the iterative approach. For more values between the left-extreme digit and median, the number of combinations also increases. 

![image](https://github.com/user-attachments/assets/ca480040-6351-43c1-b31d-2feb23130eb3)
![image](https://github.com/user-attachments/assets/c97772fe-a28c-46f0-8ebe-e039ed6b2010)


However, on the other hand, the runtime analysis is different. It is seen that the recursive takes more time to run as the input increase than the iterative. This again makes sense when thinking about the difference in running time between an inbuilt function itertools.product() (for the iterative) and the created function more than once (for the recursive). 

As pointed out by Cormen et al. (2009), an algorithm running time is defined by its number of steps (still, the number of steps should have more appropriate assumptions than those made for this assignment). Therefore when comparing the two analyses, the inference that aligns more with this definition is the best implementation (or more efficient algorithm) is the recursive algorithm. The main reason is the number of steps the itertools.product() takes. The iterative algorithm number of steps becomes increasingly higher than the recursive approach for the same input.

Since this analysis only considers values below 20 (the code takes too much time for values above 15), it might be necessary to look up the functions for more significant values. However, given the above explanation, the algorithms might behave as predicted. 

---
## **Extended Binary Search**
Binary search, where recursive and iterative Python implementations return a list with three elements (start-index, end-index, and number of matches found in the sorted array).

### Scenario
Algorithm for a post office that will send trucks to different houses in the city. The post office wants to minimize the number of trucks needed, so all the homes with the same postal code should only require one truck.

The houses' postal codes are stored in a sorted array. Many places can share the same postal code. To simplify the database, I mapped the postal codes to specific numbers. For example, 94102 has been mapped to 1. 

Given a target postal code, the task is to return the beginning and end index of this target value in the array (inclusive) and the total number of postal codes. If this postal code is not in the database, return None. For example, given the postal array [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 7], and our target 4, the answer should be [4, 6, 3], where 4 is the start-index, 6 is the end-index, and 3 is the number of postal codes of this value. If our target is 1 for the same postal array, the answer should be [0, 0, 1]. If the target is 6, the answer should be None.

### Iterative
The code compares each number in the postal array with the target number using a `for` loop. Then its position would be added to a `tracker` list. The process continues until the current number being checked is not the number of interest. We get the position of the first and the last and the counting from the `tracker` list.

### Recursive
A function takes a position value and reads the number in that position in the postal array. If it matches, I will store the value of the place and how many times the number has been reached. For the following recursion, it will change the value of the position, adding one, and the same process will continue until all the places have been checked. In the end, the first and last position of the match with the number of matches will be outputted.

### Flowchart

![Postal code algorithm](https://github.com/user-attachments/assets/7b1118db-8746-4002-b0f6-446ecac75fb7)
![Postal code algorithm (1)](https://github.com/user-attachments/assets/9fd2f531-1f22-4bdc-b819-662c71532361)

### Experimental Analysis

I used the number of steps and running time as the metrics. For the new code version, several arrays were created using the random function to increase different sizes and several target numbers. The plotted graphics show that both algorithms share a similar pattern for the number of steps, which is predictable since the recursive works by following an iterative indexing model. Therefore we should compare the running time. The iterative algorithm performs better than the recursive algorithm, as observed by the slope of the plotted functions. Thus, the best formulation is the iterative algorithm using the running time as a performative metric.

![image](https://github.com/user-attachments/assets/cd37951e-d9ee-4a84-b21f-40f71d3a743d)
![image](https://github.com/user-attachments/assets/32924405-5bcb-43ad-8d85-380011290836)

---
## Merge and Insertion Sort
Insertion sort is a very good algorithm for small arrays, while merge sort is considered one of the fastest algorithms. We would like to investigate whether we can design a better algorithm than merge sort by analyzing a variety of input distributions and sizes.

### Merge Until Insertion
Python implementation that runs merge sort until the array gets fewer than 10 elements () when it switches to applying insertion sort.

### Insertion Until Merge
Python implementation that runs insertion sort until the array gets fewer than 10 elements (), and then the remaining array is sorted using merge sort.

### Theoretical Complexity Analysis
Theoretical complexity analysis of the two algorithms I have implemented, and conveyed by the functions merge_sort_until_k and insertion_sort_until_k. 

#### Time complexity of merge_sort_until_k

The following analysis will consider the worst-case output of the algorithm.

The `merge_sort_until_k` will split the array in the middle recursively until it reaches the base case, where the split reaches a subarray of size $k$ or less. When this happens, the code will apply insertion sort in this at-maximum-k-sized array. The code will then call the `merge()` function to merge back the subarray sorted by insertion. Therefore, the code has a merge performance, but instead of reaching the base case where there is a subarray with one element, it will get a bottom where there are at least $k$ elements. In other words, considering the divide-and-conquer approach, the divide will happen until it reaches the baseline of $k$-elements and will combine as usual from there. 

The images below show a recursive tree for the time complexity of the function. It follows the behavior of a merge sort algorithm, but when it reaches the base case of $k$, it runs the insertion and merges the list again. The complexity can be calculated as the depth (number of levels) times the amount of work for each level. 

![Recursive tree for merge_sort_until_k()_page-0001](https://github.com/user-attachments/assets/7306f614-0245-45ac-8dba-7167b4268e89)

In the image, the array size is $n$, and the depth is $h$, while the work for each line is $c_n$ ($c$ is a constant, and $n$ is the complexity time to merge each pair of subarray again during the combining part). After reaching the base case $k$, the algorithm takes the constant work ($n$) to combine the subarray. We need to find $h$ in terms of $n$.

##### Finding h
As in merge, we constantly divide the input array by two until we reach $k$. Suppose we are making $h$ divisions of $n$ by two until it equals $k$. We can express this as:

$$\frac{n}{2^h} = k$$
$$n = k\times 2^h$$
$$2^h = \frac{n}{k}$$

We can isolate h by using the definition of a logarithm of base 2 (lg):

$$\lg(n/k) = h$$ 

##### Insertion sort analysis
We apply insertion sort until we reach the base case or for each $k$. Since the complexity for insertion sort is $T(n) = n^2$, we can write the insertion part as $k^2$. Because we are applying insertion sort $2^h$ times (the number of insertions), we are using insertion sort as $k^2 \times 2^h$. We can then plug in the value for $h$ found previously and find out the complexity for the insertion part in terms of $n$ and $k$.

$$k^2 \times 2^h = k^2 \times 2^{\lg(n/k)}$$
$$k^2 \times \frac{n}{k} = nk$$

We should, therefore, add the insertion sort analysis to the merge sort analysis because it does not matter $n$. We are always calling the insertion sort at the bottom level.

##### Final analysis
Once we have $h$, we can find the time complexity for the complexity of the `merge_sort_until_k` function:

$$T(n) = n\times h + nk$$

$$T(n) = n\times \lg(n/k) + nk$$
or
$$T(n) = O(n\times\lg(n/k) + nk)$$

Where $n$ is the input size and $k$ is the merge and insertion sort threshold.

#### Time complexity of insertion_sort_until_k

The complexity for the `insertion_sort_until_k` is more intuitive. 
Considering the worst-case output for the algorithm when $n > k4, we will always apply insertion for $n-k$ input size, and the remaining will call merge ($k$ input size). For the insertion sort, we will have a behavior of $(n-k)^2$ since only the array with input size $n-k$ will go under insertion. And then, the remaining ($k$) will go under merge sort. Therefore it will be $k\times\lg(k)$, where $\lg$ is the log of base 2.

However, in the code implementation, it was possible to see that after the sorting by insertion and merge sort of parts of the initial array, we are still merging the entire array again by calling merge sort. Since the final array is still going under merge sort (which is counterintuitive since it goes against the optimization of the algorithm, making it work more by adding two additional terms), we are still adding a third term $n\times\lg(n)$.

Therefore the final time complexity analysis for `insertion_sort_until_k` is:

$$T(n) = (n-k)^2 + k\times\lg(k) + n\times\lg(n)$$
or 
$$T(n) = O((n-k)^2 + k\times\lg(k) + n\times\lg(n))$$

The first term is the insertion sort application of the first $n-k$ elements, the second is the merge sort application of the final $k$ element, and the third is the final merge sort application of the entire list.

### Experimental Analysis
Which algorithm should one choose for the same input and $k=10$? How would this answer change as $k$ changes for a large input size and different inputs? How should we consider this analytically (by using insights from the analysis), experimentally (specifically, $k=5$ and $k=30$), 
and by using at least two different metrics to evaluate efficiency.

#### Analytically
From the previous item, it is possible to see that `insertion_sort_until_k` has the worst long-term behavior than any other algorithm seen so far. It is worse than the `merge_sort_until_k`, merge sort, and insertion sort. This is because the time complexity function, as demonstrated, shows an $n$-squared term and two $n\times\lg(n)$ terms. Depending on the number of $k$, `insertion_sort_until` can perform slightly better. When $k$ approaches $n$, `insertion_sort_until_k` will get to approach the performance of merge sort.

Conversely, the `merge_sort_until_k` will perform better since it has a leading term $n\times\lg(n/k)$ plus a constant term $n\times k$. The logarithm term performs better than the usual merge because $n$ is divided by $k$, but the $n\times k$ term might offset the expected outcome. $k$ has to be a positive number less or equal to $n$. If $k$ is equal to $n$, we will have $n^2$, or an insertion sort behavior, in order terms, the worst case. So `merge_sort_until_k` performs better for small values of $k$.

#### Experimentally by Efficiency
The plots below will analyze the asymptotic behavior of both functions by scaling the average running time and the number of steps to evaluate the algorithm efficiency. It tested different $k$ values, including 5 and 30, but the one left was $k=5$ for both analyses.

##### Time Efficiency
The time efficiency for both algorithms was calculated by plotting the average time each algorithm took to run for increased input size for random inputs. By using random inputs, the algorithm scales for the average output cases. Then it is not expected that either the best or worst-case output is going to happen. By using randomization, the algorithm is likely to perform in a natural setting where the input list is unordered but not in any extreme cases (purely sorted or sorted in descending order). By doing this, the analysis gets closer to reality and therefore becomes more accurate.

![image](https://github.com/user-attachments/assets/cb003970-5941-45ae-96b4-6b8f5c624041)

As inferred from the plot, the `merge_sort_until_k` performs better than the `insertion_sort_until_k` when $k$ is a small number (5 in this case). This happens because, for `insertion_sort_until_k`, the code will perform insertion of $n-k$ numbers (input size minus $k$) and then perform merge sort in the remaining $k$ values and again merge the entire list. So when $k$ is small when compared to the input size, the algorithm has an insertion sort behavior $(n^2)$ for more significant inputs. Adding the merge sort will not be counted at the scaling since the insertion behavior will be the leading factor. The insertion sort will still be applied even for a more significant number of $k$ compared to the input size. This, however, should be different when the value of $k$ is bigger than the input size for `insertion_sort_until_k`. However, by running the plots for this case, the scaling time behavior does not improve considerably as expected.

On the other side, the time scaling behavior for `merge_sort_until_k` is expected, as shown because it will split the list by applying merge sort until reaching the bottom case, which is $k$, and then using insertion sort. After that, it merges the elements again. In this case, the insertion sort will always happen but will not happen for a big part of the array as in `insertion_sort_until_k`. Because the dividing approach will divide the array into small arrays, the application of insertion sort will be efficient concerning time since insertion sort is expected to take less time than merge sort for a small input size. After the application of insertion, the merge will finish its job by merging the array back. Merge gets better for higher values of $k$ when compared to the input size. This makes sense since, for larger input sizes, only one part of the code will be called the insertion one.

Therefore, from the time analysis, it is possible to see that `merge_sort_until_k` will perform better than the `insertion_sort_until_k` for any given $k$. 

#### Step Counts
The step count efficiency analysis follows the same behavior as the time complexity analysis for small values of $k$. `merge_sort_until_k` performs better than the `insertion_sort_until_k` when $k$ is small enough; for example, when $k=5$, both behavior will be linear, but the `merge_sort_until_k` will have a behavior closer to constant than the `insertion_sort_until_k`. However, when $k$ is big enough, for example, when $k$ is equal to the input size, insertion will perform way better than the merge sort. Insertion will be almost constant, while merge appears to have quadratic behaviors. This is what was expected to see in the time analysis. For high $k$, insertion will behave way better than merge because insertion will behave as merge while merge will behave as insertion. Here they will perform their asymptotic behavior as expected. $O(n^2)$ for merge that will act as insertion, and $O(n\times\lg(n))$ for insertion that will act as merge.

![image](https://github.com/user-attachments/assets/3c3c90d6-6ec1-49a4-b721-a096afd24cec)

### Conclusion
From both the analytical and experimental analysis, it was possible to conclude that `merge_sort_until_k` will perform better than `insertion_sort_until_k` for any small given $k$ compared to the input size. But when $k$ gets close to or greater than the input size, the merge sort will behave as insertion, assuming its scaling behavior of $O(n^2)$, while the insertion will behave as merge getting its behavior of $O(n\times\lg(n))$. Both explanations were given mathematically by explaining the formula for the time complexity and experimentally by taking tests and drawing plots for increased input size for random inputs. The use of randomization was also described as a tool to resemble reality better since it is rare that one of the extreme cases (fully sorted or sorted in descending order inputs) will happen frequently.

To better understand why merge sort is preferred until a specific $k$ value, here is an example:
For an array with size 100, if $k$ is smaller than 100, the merge sort is expected to behave better than insertion because the merge part will still happen, letting just a tiny part be sorted by insertion. In contrast, the insertion will happen pretty much for a big part of the `insertion_sort_until_k`. However, when $k$ gets close to 100, or when $k$ is greater than 100, insertion sort should be preferred because the `merge_sort_until_k` will only call insertion since $k$ (the bottom level) is already the entire list. And no merge will be called at all. On the other hand, for this same value of $k$, `insertion_sort_until_k` will behave as merge sort because no insertion will be applied, only merge sort.

---
## References
Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2009). Introduction to Algorithms (Third). Cambridge, Mass.: Mit Press.

