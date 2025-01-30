# Strobogrammatic Number Generator and Experimental Analysis
A strobogrammatic number is a number that looks the same when rotated upside down, such as 8, 101, 96. Here we consider 1 to be strobogrammatic.
I developed two codes using a **iterative** and **recursive** approach that takes an integer _n_ as input and returns all the strobogrammatic numbers of length _n_ in a list.

## Iterative Approach

In the iterative approach, if the number of digits is 1, the strobogrammatic number can be either 0, 1, or 8. 

For digits greater than 2, we first define the extreme values as 1-1, 8-8, 6-9, or 9-6 (it cannot be 0 since the digit number would be less than expected). Then, for each empty place in the first half of the digits, between the left-extreme and the median (if the digit number is odd), we calculate the Cartesian product. Cartesian product of two sets $A \times B$ is the set of all the ordered pairs $(a, b)$ such that $a$ belongs to $A$ and $b$ belongs to $B$. This approach would extend the number of Cartesian product factors (or initial sets $A \times B \times C \times \dots$) to the number of places between the left-extreme and the median (both exclusive), where its elements could only assume values of (0, 1, 8, 6, 9). We would assign each combination generated $(a, b, c, \dots)$ as a strobogrammatic for each extreme-values combination. The second half of digits, after the median and before the right-extreme, would be defined as the mirrored value of its complementary. 

If the digit number is odd, a center value will be added for each combination generated. This value would assume either 0, 1, or 8. If the digit number is even, such a center value would not exist, and the code would be done, outputting all numbers.

## Recursive Approach

If the length of a strobogrammatic number is 1, there are only three possible possibilities. The number can be 0, 1, or 8. However, when the number of digits is greater than 1, the number can be composed of 6 and 9 (and vice-versa) when they are equidistant concerning the median digit.

A better way to create such numbers from a recursive approach is by defining a sub-function that can be called for when the input size is bigger than 1. This function should define the extremities of the numbers to be either (1-1, 8-8, 6-9, or 9-6). These extremes would be disregarded for the recursion input, and then the subfunction would be called to return for the inner values for the new extremities. However, the values would now consider the equidistant pair 0-0. Therefore, its values would assume the (0-0, 1-1, 8-8, 6-9, 9-6) pairs. The code ends when the function reaches the base case: the center values, which can be either (0, 1, 8) if the input size is odd, or (00, 11, 88, 69, 96) when it is even.

## Flowchart
![strobogrammatic() (1)](https://github.com/user-attachments/assets/d91b051b-54c7-41c9-bfdf-ee3d25b8eb33)
![strobogrammatic() (2)](https://github.com/user-attachments/assets/245a2443-aadd-4920-bf51-52462641de97)


## Experimental Analysis
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



## References
Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2009). Introduction to Algorithms (Third). Cambridge, Mass.: Mit Press.

