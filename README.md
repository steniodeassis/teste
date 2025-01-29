# Data Structures and Algorithms

Codes from assignments of Data Structures and Algorithms class.

## Strobogrammatic number
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
![pdf](https://minerva-sle-collaboration-production.s3.us-west-2.amazonaws.com/workbook-upload/cl84j80ko0000356hkxboq50d)
