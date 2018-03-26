# algorithms-in-python
In this respository, I implemented some famous alogritms using python. I arrange them according to the strategy they use. And for every algorithn, I will explain the problem they try to solve and some relevant resourses.<br>
(The main idea for this respository is to review all these brilliant algorithms and make a beautiful README for them.)
## 1.0 - Divide and Conquer
This section, I will talk about the famous divide and conquer strategy and show some applications of this strategy.
### 1.1 - Interger Multiplication Problem [Link](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
![Interger_MUL][Interger_MUL1]

[Interger_MUL1]: ./images/integer_mult.png
The standard procedure for multiplication of two n-digit numbers requires a number of elementary operations proportional to ${\displaystyle O(n^{2})}$. As for The Karatsuba algorithm, it reduces the running time to at most ${\displaystyle n^{\log _{2}3}\approx n^{1.585}}$ <br>

<strong>Key idea</strong> <br>
The basic step of Karatsuba's algorithm is a formula that allows one to compute the product of two large numbers ${\displaystyle x}$ and ${\displaystyle y}$ using three multiplications of smaller numbers, each with about half as many digits as ${\displaystyle x}$ or ${\displaystyle y}$, plus some additions and digit shifts. <br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)=\Theta (n^{\log _{2}3})\,\!$
### 1.2 - Merge Sort (and Insertion Sort) [Link](https://en.wikipedia.org/wiki/Merge_sort)
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
### 1.3 - Count Inversions [Link](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/05DivideAndConquerI.pdf)
Actually, this can be treated as application of Merger Sort. Every time we do merge operation in merge sort, we implicitly calculate the inversions. <br>
![inversion][inversion1]

[inversion1]: ./images/inversions.png
<strong>Key idea</strong> <br>
Like the figure above, when we first take in element from right sub-array in merge operation, that indicates the right element is smaller than ( length of left sub-array - the index of left element) elements. <br>
As the algorithm progresses, add all the inversions will give us the total inversions.<br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(n{\log n})\,\!$

### 1.4 - Maximum Subarray [Link](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
The maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array, a[1...n], of numbers which has the largest sum. <br>
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
This section I will talk about two algorithms which has used random variable inside.
### 2.1 - Quick Sort [Link](https://en.wikipedia.org/wiki/Quicksort)
![quick][quick1]

[quick1]: ./images/Sorting_quicksort_anim.gif
<strong>Key idea</strong> <br>
Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements relative to a randomly chosen element. Quicksort can then recursively sort the sub-arrays. So, the key point in quick sort is to choose partition element. <br>
<strong>Propeties</strong> <br>
* Worst case performance	O(n^2)
* Best case performance	O(n log n) or O(n) with three-way partition
* Average case performance	O(n log n)
### 2.2 - Karger's Algorithm [Link](https://en.wikipedia.org/wiki/Karger%27s_algorithm)
The idea of the algorithm is based on the concept of contraction of an edge $(u,v)$ in an undirected graph $G=(V,E)$. Informally speaking, the contraction of an edge merges the nodes $u$ and $v$ into one, reducing the total number of nodes of the graph by one.
The figure below shows how contraction works. In the sub figure left, two Bold Black nodes are fused into one (the sub figure in the right).
![karger][karger1]

[karger1]: ./images/example_kar.png
<strong>Key idea</strong> <br>
By repeating the contraction algorithm $T={\binom  {n}{2}}\ln n$ times with independent random choices and returning the smallest cut, the probability of not finding a minimum cut is
${\displaystyle \left[1-{\binom {n}{2}}^{-1}\right]^{T}\leq {\frac {1}{e^{\ln n}}}={\frac {1}{n}}\,.}$ <br>
<strong>Propeties</strong> <br>
* With high probability we can find all min cuts in the running time of $O(n^{2}\ln ^{3}n)$ 
* Not finding a min cut probability is ${\frac {1}{n}}$ after $T={\binom  {n}{2}}\ln n$ times.

## 3.0 - Data Structures
It may be misleading to put data structure as a independent section. However, I want to introduce some kind of complicate problems which can be solved so elegantly using proper data strutures. Of course, they may contain some algorithm design strategies that are not talked about yet.
### 3.1 - Queue and Breadth First Search [Link1](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) [Link2](https://en.wikipedia.org/wiki/Breadth-first_search)
Queue, also known as FIFO, is an acronym for first in, first out, a method for organizing and manipulating a data buffer, where the oldest (first) entry, or 'head' of the queue, is processed first.
![queue][queue1]

[queue1]: ./images/Fifo_queue.png

<strong>Key idea</strong> <br>
And BFS is used in undirected or directed graph and it tells how many nodes a source node can reach and print them out by the order we find them. We use queue to store the nodes we color grey(see the gif below). As for the "breadth" in its name, it means we try to find a reachable node using the shortest length. And the border between visited nodes and undiscovered nodes is extended by its breadth.

![bfs][bfs1]

[bfs1]: ./images/Animated_BFS.gif

<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(V+E)$, $V$ is number of vertices, $E$ is number of edges

### 3.2 - Stack and Depth First Search [Link1](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) [Link2](https://en.wikipedia.org/wiki/Depth-first_search)
Stack, also known as LIFO, has the property of last in, first out.
![stack][stack1]

[stack1]: ./images/Lifo_stack.png

<strong>Key idea</strong> <br>
And DFS is used in directed graph and it tells how many nodes a source node can reach and print them out by the order we find them. We use stack to store the nodes we classify as the start points for graph. The "depth" in its name means that this algorithm will go as deeply as it can for a given source and when it reaches the endpoint, it returns to the start node.

![depth][depth1]

[depth1]: ./images/Depth-First-Search.gif

<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(V+E)$, $V$ is number of vertices, $E$ is number of edges

### 3.3 - Heap and Median Median Maintenance [Link1](https://en.wikipedia.org/wiki/Heap_(data_structure))[Link2](https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/)
Heap is a specialized tree-based data structure that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C.[1] The node at the "top" of the heap (with no parents) is called the root node.

![heap][heap1]

[heap1]: ./images/Max-Heap.png

Median Maintenance problem is that if integers are read from a data stream, find median of elements read so for in efficient way. For simplicity assume there are no duplicates. <br>

<strong>Key idea</strong> <br>
We can use a max heap on left side to represent elements that are less than effective median, and a min heap on right side to represent elements that are greater than effective median. When the difference between size of two heaps is greater or equal to 2, we switch one element to another smaller size heap.

<strong>Propeties</strong> <br>
* Running Time: $T(n)= O(N log N)$

### 3.4 - Strongly Connected Component [Link](https://en.wikipedia.org/wiki/Strongly_connected_component)
A directed graph is called strongly connected if there is a path in each direction between each pair of vertices of the graph. In a directed graph G that may not itself be strongly connected, a pair of vertices u and v are said to be strongly connected to each other if there is a path in each direction between them.

![scc][scc1]

[scc1]: ./images/Scc.png

<strong>Key idea</strong> <br>
Through simple observation, we find out that tranpose of graph has the same SCCs as the original graph. We run DFS twice. First time, we run it on G and compute finishing time for each vertex. And then, we run DFS on G^T but in the main loop of DFS, consider the vertices in order of decreasing finishing time. <br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)= \theta(V+E)$, $V$ is number of vertices, $E$ is number of edges

### 3.5 - Disjoint-set and SCC [Link](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
A disjoint-set data structure, also called a union–find data structure or merge–find set, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. <br>
For a naive disjoint-set, it supports two main operations, Make-Set and Union. Make-set make every vertex an independent group. Union puts two vertices in one group.

![union][union1]

[union1]: ./images/unionfind.png

<strong>Key idea</strong> <br>
In an undirected graph, we can use this data structure to find out how many SCCs. The figure below shows how it works.

![scc_uf][scc_uf1]

[scc_uf1]: ./images/uf.png



<strong>Propeties</strong> <br>
* We can use a weighted-union heuristic to save time when call find_set operation
* Path compression can greatly improve time efficiency of union find

## 4.0 - Greedy Algorithms
In this section, I'm going to introducce greedy algorithms, one powerful algorithms design strategy. <br>
From [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm), a greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage[1] with the hope of finding a global optimum. In many problems, a greedy strategy does not in general produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a global optimal solution in a reasonable time.
### 4.1 - Shedule Activities [Link](https://en.wikipedia.org/wiki/Activity_selection_problem)
In activity selection problem, every activity has its own weight and length. And our goal is to minimize the sum of weight\*length.
It is a very easy and great example to show how greedy algorithm works and provide an elegant proof using argument exchange technique. <br>
<strong>Key idea</strong> <br>
If we sort activity by value weight/length, we can prove an existing optimal structure cannot be better than this arrangement.
![act][act1]

[act1]: ./images/act1.png

<img src=" ./images/act1.png" style="zoom:50%" />


### 4.2 - Huffman Coding [Link](https://en.wikipedia.org/wiki/Huffman_coding)
Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. 
For example, the table below shows letters' frequency in a "book".

![freq][freq1]

[freq1]: ./images/freq.png
One way to encode this book is to use fixed length coding. As shown below:

![fixed][fixed1]

[fixed1]: ./images/fixed.png

As for huffman coding, the actual tree structure looks like this:

![huff][huff1]

[huff1]: ./images/huff.png

<strong>Key idea</strong> <br>
We maintain a binary tree and create a new node as the parent for two least-frequent letters. And the key for this new node is the sum of keys for its two children. We repeat this until no nodes left in this "book".

![huff_works][huff_works1]

[huff_works1]: ./images/huff_works.png

<strong>Properties</strong> <br>
* Procedure HUFFMAN produces an optimal prefix code
