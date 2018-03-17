# algorithms-in-python
In this respository, I implemented some famous alogritms using python. I arrange them according to the strategy they use. And for every algorithn, I will explain the problem they try to solve and some relevant resourses.<br>
(The main idea for this respository is to review all these brilliant algorithms and make a beautiful README for them.)
## 1.0 - Divide and Conquer
### 1.1 - Interger Multiplication Problem [Link](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
![Interger_MUL][Interger_MUL1]

[Interger_MUL1]: ./images/integer_mult.png
The standard procedure for multiplication of two n-digit numbers requires a number of elementary operations proportional to ${\displaystyle O(n^{2})}$. As for The Karatsuba algorithm, it reduces the running time to at most ${\displaystyle n^{\log _{2}3}\approx n^{1.585}}$ <br>

<strong>Key idea</strong> <br>
The basic step of Karatsuba's algorithm is a formula that allows one to compute the product of two large numbers ${\displaystyle x}$ and ${\displaystyle y}$ using three multiplications of smaller numbers, each with about half as many digits as ${\displaystyle x}$ or ${\displaystyle y}$, plus some additions and digit shifts. <br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)=\Theta (n^{\log _{2}3})\,\!$
### 1.2 - Merge Sort [Link](https://en.wikipedia.org/wiki/Merge_sort)
Before we talk about merge sort. First take a look at another algorithm and its running time to fully appreciate how great merge sort is.
One intuitive idea for sorting is to imitate how we arrange cards according to their size, like the picture below. We immediately arrange the card when we receive it just based on what we have on our hands.
![insert][insert1]

[insert1]: ./images/insert.png
And the worst running time for this alogorithm is $T(n)= \theta (n^{2})\,\!$. <br>
Gif above shows how merge sort works:
![merge][merge1]

[merge1]: ./images/Merge-sort-example-300px.gif

<strong>Key idea</strong> <br>
Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted) and repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.<br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(n{\log n})\,\!$
### 1.2 - Count Inversions [Link](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/05DivideAndConquerI.pdf)
Actually, this can be treated as application of Merger Sort. Every time we do merge operation in merge sort, we implicitly calculate the inversions.
![inversion][inversion1]

[inversion1]: ./images/inversions.png
<strong>Key idea</strong> <br>
Like the figure above, when we first take in element from right sub-array in merge operation, that indicates the right element is smaller than the length of left sub-array minus the index of left element. <br>
As the algorithm progresses, add all the inversions will give us the total inversions.<br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(n{\log n})\,\!$

### 1.3 - Maximum Subarray [Link](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
The maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array, a[1...n], of numbers which has the largest sum.
<strong>Key idea</strong> <br>
If we use the divide and conquer strategy, if the array is A[low..high] and the middle point is represented as mid. A[i..j]is what we want to calcualte. A[i..j] has to be one of the three cases:<br>
- A[i..j] belongs to A[low..mid]
- A[i..j] belongs to A[mid+1..high]
- i <= mid < j <br>
So, our job is to find the largest sub array crossing the mid point and choose the largest one among these three algorithms.
![cross][cross1]

[cross1]: ./images/max_crossing1.png
<strong>Propeties</strong> <br>
* Running Time: $T(n)= \theta(n{\lg n})\,\!$

## 2.0 - Randomized Algorithms
### 2.1 - Quick Sort [Link](https://en.wikipedia.org/wiki/Quicksort)
![quick][quick1]

[quick1]: ./images/Sorting_quicksort_anim.gif
<strong>Key idea</strong> <br>
Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements relative to a randomly chosen element. Quicksort can then recursively sort the sub-arrays. So, the key point in quick sort is to choose partition element.
<strong>Propeties</strong> <br>
* Worst case performance	O(n^2)
* Best case performance	O(n log n) or O(n) with three-way partition
* Average case performance	O(n log n)
