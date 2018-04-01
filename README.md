# algorithms-in-python
This repository, I will use Python to implement some famous algorithms. The algorithms are arranged according to the strategy used.
Each algorithm will have an explanation to the problem it attempts to solves and some relevant resources.<br>
(The goal of this repository is to create a beautiful README for all of these brilliant algorithms that I have reviewed.) <br> <br>
<strong><font size=8>Content:</font></strong>
<a id="head"/>
* [1.0 - Divide and Conquer](#10---divide-and-conquer)
  * [1.1 - Interger Multiplication Problem](#11---interger-multiplication-problem)
  * [1.2 - Merge Sort (and Insertion Sort)](#12---merge-sort-and-insertion-sort)
  * [1.3 - Count Inversions](#13---count-inversions)
  * [1.4 - Maximum Subarray](#14---maximum-subarray)
* [2.0 - Randomized Algorithms](#20---randomized-algorithms)
  * [2.1 - Quick Sort](#21---quick-sort)
  * [2.2 - Karger's Algorithm](#22---karger-algorithm)
* [3.0 - Data Structures](#30---data-structures)
  * [3.1 - Queue and Breadth First Search](#31---queue-and-breadth-first-search)
  * [3.2 - Stack and Depth First Search](#32---stack-and-depth-first-search)
  * [3.3 - Heap and Median Median Maintenance](#33---heap-and-median-median-maintenance)
  * [3.4 - Strongly Connected Component](#34---strongly-connected-component)
  * [3.5 - Disjoint-set and SCC](#35---disjoint-set-and-scc)
* [4.0 - Greedy Algorithms](#40---greedy-algorithms)
  * [4.1 - Shedule Activities](#41---shedule-activities)
  * [4.2 - Activity selection](#42---activity-selection)
  * [4.3 - Huffman Coding](#43---huffman-coding)
  * [4.4 - Dijkstra's Algorithm](#44---dijkstra-algorithm)
  * [4.5 - Prim's Algorithm](#45---prim-algorithm)
  * [4.6 - Kruskal's Algorithm and Clustering Problem](#46---kruskal-algorithm-and-clustering-problem)
* [5.0 - Dynamic Programming](#50---dynamic-programming)
  * [5.1 - Rod Cutting](#51---rod-cutting)
  * [5.2 - Matrix Chain Multiplication](#52---matrix-chain-multiplication)
  * [5.3 - Longest Common Subsequence](#53---longest-common-subsequence)
  * [5.4 - Floyd-Warshall Algorithm](#54---floyd-warshall-algorithm)
* [6.0 - Approximation Algorithms for NPC](#60---approximation-algorithms-for-npc)
  * [6.1 - Vertex Cover](#61---vertex-cover)
  * [6.2 - Travelling Salesman Problem](#62---travelling-salesman-problem)
  * [6.3 - Boolean Satisfiability Problem](#63---boolean-satisfiability-problem)


## 1.0 - Divide and Conquer
This section, I will talk about the famous divide and conquer strategy and show some applications of this strategy.
### 1.1 - Interger Multiplication Problem
* Useful [Link](https://en.wikipedia.org/wiki/Karatsuba_algorithm) <br>
![Interger_MUL][Interger_MUL1]

[Interger_MUL1]: ./images/integer_mult.png
The standard procedure for multiplication of two n-digit numbers requires a number of elementary operations proportional to ![equation](http://latex.codecogs.com/gif.latex?O(n^{2})). As for The Karatsuba algorithm, it reduces the running time to at most ![equation](http://latex.codecogs.com/gif.latex?n^{\log%20_{2}3}\approx%20n^{1.585}) <br>

<strong>Key idea</strong> <br>
The basic step of Karatsuba's algorithm is a formula that allows one to compute the product of two large numbers ![equation](http://latex.codecogs.com/gif.latex?x) and ![equation](http://latex.codecogs.com/gif.latex?y) using three multiplications of smaller numbers, each with about half as many digits as ![equation](http://latex.codecogs.com/gif.latex?x) or ![equation](http://latex.codecogs.com/gif.latex?y), plus some additions and digit shifts. <br>
<strong>Propeties</strong> <br>
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=\Theta%20(n^{\log%20_{2}3})) <br>
<a href="#head">`Back to Top`</a>
### 1.2 - Merge Sort and Insertion Sort
* Useful [Link](https://en.wikipedia.org/wiki/Merge_sort) <br>
Before we talk about merge sort. First take a look at another algorithm and its running time to fully appreciate how great merge sort is.
One intuitive idea for sorting is to imitate how we arrange cards according to their size, like the picture below. We immediately arrange the card when we receive it just based on what we have on our hands.
![insert][insert1]

[insert1]: ./images/insert.png
And the worst running time for this alogorithm is ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20\theta%20(n^{2})). <br>
Gif above shows how merge sort works:
![merge][merge1]

[merge1]: ./images/Merge-sort-example-300px.gif

<strong>Key idea</strong> <br>
Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted) and repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.<br>
<strong>Propeties</strong> <br>
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20O(n{\log%20n})) <br>
<a href="#head">`Back to Top`</a>
### 1.3 - Count Inversions
* Useful [Link](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/05DivideAndConquerI.pdf) <br>
Actually, this can be treated as application of Merger Sort. Every time we do merge operation in merge sort, we implicitly calculate the inversions. <br>
![inversion][inversion1]

[inversion1]: ./images/inversions.png
<strong>Key idea</strong> <br>
Like the figure above, when we first take in element from right sub-array in merge operation, that indicates the right element is smaller than ( length of left sub-array - the index of left element) elements. <br>
As the algorithm progresses, add all the inversions will give us the total inversions.<br>
<strong>Propeties</strong> <br>
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20O(n{\log%20n})) <br>
<a href="#head">`Back to Top`</a>

### 1.4 - Maximum Subarray
* Useful [Link](https://en.wikipedia.org/wiki/Maximum_subarray_problem) <br>
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
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20\theta(n{\lg%20n})) <br>
<a href="#head">`Back to Top`</a>

## 2.0 - Randomized Algorithms
This section I will talk about two algorithms which has used random variable inside.
### 2.1 - Quick Sort
* Useful [Link](https://en.wikipedia.org/wiki/Quicksort) <br>
![quick][quick1]

[quick1]: ./images/Sorting_quicksort_anim.gif
<strong>Key idea</strong> <br>
Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements relative to a randomly chosen element. Quicksort can then recursively sort the sub-arrays. So, the key point in quick sort is to choose partition element. <br>
<strong>Propeties</strong> <br>
* Worst case performance	O(n^2)
* Best case performance	O(n log n) or O(n) with three-way partition
* Average case performance	O(n log n) <br>
<a href="#head">`Back to Top`</a>
### 2.2 - Karger Algorithm
* Useful [Link](https://en.wikipedia.org/wiki/Karger%27s_algorithm) <br>
The idea of the algorithm is based on the concept of contraction of an edge (u,v) in an undirected graph G=(V,E). Informally speaking, the contraction of an edge merges the nodes u and v into one, reducing the total number of nodes of the graph by one.
The figure below shows how contraction works. In the sub figure left, two Bold Black nodes are fused into one (the sub figure in the right).
![karger][karger1]

[karger1]: ./images/example_kar.png
<strong>Key idea</strong> <br>
By repeating the contraction algorithm ![equation](http://latex.codecogs.com/gif.latex?T={\binom%20{n}{2}}\ln%20n) times with independent random choices and returning the smallest cut, the probability of not finding a minimum cut is
![equation](http://latex.codecogs.com/gif.latex?\left[1-{\binom%20{n}{2}}^{-1}\right]^{T}\leq%20{\frac%20{1}{e^{\ln%20n}}}={\frac%20{1}{n}}.) <br>
<strong>Propeties</strong> <br>
* With high probability we can find all min cuts in the running time of ![equation](http://latex.codecogs.com/gif.latex?O(n^{2}\ln%20^{3}n))
* Not finding a min cut probability is ![equation](http://latex.codecogs.com/gif.latex?{\frac%20{1}{n}}$%20after%20$T={\binom%20{n}{2}}\ln%20n) times. <br>
<a href="#head">`Back to Top`</a>

## 3.0 - Data Structures
It may be misleading to put data structure as a independent section. However, I want to introduce some kind of complicate problems which can be solved so elegantly using proper data strutures. Of course, they may contain some algorithm design strategies that are not talked about yet.
### 3.1 - Queue and Breadth First Search
* Useful [Link1](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) [Link2](https://en.wikipedia.org/wiki/Breadth-first_search) <br>
Queue, also known as FIFO, is an acronym for first in, first out, a method for organizing and manipulating a data buffer, where the oldest (first) entry, or 'head' of the queue, is processed first.
![queue][queue1]

[queue1]: ./images/Fifo_queue.png

<strong>Key idea</strong> <br>
And BFS is used in undirected or directed graph and it tells how many nodes a source node can reach and print them out by the order we find them. We use queue to store the nodes we color grey(see the gif below). As for the "breadth" in its name, it means we try to find a reachable node using the shortest length. And the border between visited nodes and undiscovered nodes is extended by its breadth.

![bfs][bfs1]

[bfs1]: ./images/Animated_BFS.gif

<strong>Propeties</strong> <br>
* Running Time: T(n)= O(V+E), V is number of vertices, E is number of edges <br>
<a href="#head">`Back to Top`</a>

### 3.2 - Stack and Depth First Search
* Useful [Link1](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) [Link2](https://en.wikipedia.org/wiki/Depth-first_search) <br>
Stack, also known as LIFO, has the property of last in, first out. <br>
![stack][stack1]

[stack1]: ./images/Lifo_stack.png

<strong>Key idea</strong> <br>
And DFS is used in directed graph and it tells how many nodes a source node can reach and print them out by the order we find them. We use stack to store the nodes we classify as the start points for graph. The "depth" in its name means that this algorithm will go as deeply as it can for a given source and when it reaches the endpoint, it returns to the start node.

![depth][depth1]

[depth1]: ./images/Depth-First-Search.gif

<strong>Propeties</strong> <br>
* Running Time: T(n)= O(V+E), V is number of vertices, E is number of edges <br>
<a href="#head">`Back to Top`</a>

### 3.3 - Heap and Median Median Maintenance
* Useful [Link1](https://en.wikipedia.org/wiki/Heap_(data_structure)) [Link2](https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/) <br>
Heap is a specialized tree-based data structure that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C.[1] The node at the "top" of the heap (with no parents) is called the root node.

![heap][heap1]

[heap1]: ./images/Max-Heap.png

Median Maintenance problem is that if integers are read from a data stream, find median of elements read so for in efficient way. For simplicity assume there are no duplicates. <br>

<strong>Key idea</strong> <br>
We can use a max heap on left side to represent elements that are less than effective median, and a min heap on right side to represent elements that are greater than effective median. When the difference between size of two heaps is greater or equal to 2, we switch one element to another smaller size heap.

<strong>Propeties</strong> <br>
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20O(N%20log%20N)) <br>
<a href="#head">`Back to Top`</a>

### 3.4 - Strongly Connected Component
* Useful [Link](https://en.wikipedia.org/wiki/Strongly_connected_component) <br>
A directed graph is called strongly connected if there is a path in each direction between each pair of vertices of the graph. In a directed graph G that may not itself be strongly connected, a pair of vertices u and v are said to be strongly connected to each other if there is a path in each direction between them.

![scc][scc1]

[scc1]: ./images/Scc.png

<strong>Key idea</strong> <br>
Through simple observation, we find out that tranpose of graph has the same SCCs as the original graph. We run DFS twice. First time, we run it on G and compute finishing time for each vertex. And then, we run DFS on G^T but in the main loop of DFS, consider the vertices in order of decreasing finishing time. <br>
<strong>Propeties</strong> <br>
* Running Time: ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20\theta(V+E)), V is number of vertices, E is number of edges <br>
<a href="#head">`Back to Top`</a>

### 3.5 - Disjoint-set and SCC
* Useful [Link](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) <br>
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
* Path compression can greatly improve time efficiency of union find <br>
<a href="#head">`Back to Top`</a>

## 4.0 - Greedy Algorithms
In this section, I'm going to introducce greedy algorithms, one powerful algorithm design strategy. <br>
From [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm), a greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage[1] with the hope of finding a global optimum. In many problems, a greedy strategy does not in general produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a global optimal solution in a reasonable time.
### 4.1 - Shedule Activities
In activity selection problem, every activity has its own weight and length. And our goal is to minimize the sum of weight\*length.
It is a very easy and great example to show how greedy algorithm works and provide an elegant proof using argument exchange technique. <br>
<strong>Key idea</strong> <br>
If we sort activity by value weight/length, we can prove an existing optimal structure cannot be better than this arrangement.
![act][act1]

[act1]: ./images/act1.png

As the figure shown above, we consider the cost caused by two activites that are ranged differently in two arrangement (i, j). We find out that the cost in greedy alogrithm is smaller than optimal structure by the value of wi\*lj - wj\*li, which is greater than or equat to 0.

<strong>Properties</strong> <br>
* Running time is dominated by sorting <br>
<a href="#head">`Back to Top`</a>

### 4.2 - Activity selection
* Useful [Link](https://en.wikipedia.org/wiki/Activity_selection_problem) <br>
In this problem, every activity has its own start time and finish time. our goal is to selection a max-length subset, where jobs are compatible. <br>

![selection][selection1]

[selection1]: ./images/selection.png

<strong>Key idea</strong> <br>
We sorted the array according to its finish time.
The alogirthm put the first job whose start time is bigger than last job's finish time. <br>
<strong>Properties</strong> <br>
* The recursive activity selection running time is ![equation](http://latex.codecogs.com/gif.latex?T(n)=%20\theta(n)) <br>
<a href="#head">`Back to Top`</a>

### 4.3 - Huffman Coding
* Useful [Link](https://en.wikipedia.org/wiki/Huffman_coding) <br>
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
* Procedure HUFFMAN produces an optimal prefix code <br>
<a href="#head">`Back to Top`</a>

### 4.4 - Dijkstra Algorithm
* Useful [Link](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) <br>

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. However, it has one prerequisite, all paths have to be greater or equal to 0.

![dij][dij1]

[dij1]: ./images/Dijkstra_Animation.gif

<strong>Key idea</strong> <br>
Seperate nodes into two groups, one group is marked as explored. And we update the distance from unexplored group to explored group by the shortest distance.

<strong>Properties</strong> <br>
* Running time ![equation](http://latex.codecogs.com/gif.latex?O(|E|+|V|\log%20|V|)) based on a min-priority queue implemented by a Fibonacci heap <br>
<a href="#head">`Back to Top`</a>

### 4.5 - Prim Algorithm
* Useful [Link](https://en.wikipedia.org/wiki/Prim%27s_algorithm) <br>
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. Very similar to Dijkstra Algorithm, we maintain two sets, explored one and unexplored one. Every time, we only absorb the vertex, which has the smallest distance to explored set. This is shown very clearly in the figure below:

![prim][prim1]

[prim1]: ./images/prim.gif

<strong>Key idea</strong> <br>
The algorithm may informally be described as performing the following steps:

Initialize a tree with a single vertex, chosen arbitrarily from the graph. <br>
Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree. <br>
Repeat step 2 (until all vertices are in the tree). <br>

<strong>Properties</strong> <br>

* Running time
 + adjacency matrix, searching	![equation](http://latex.codecogs.com/gif.latex?O(|V|^2))
 + binary heap and adjacency list	![equation](http://latex.codecogs.com/gif.latex?O((|V|+|E|)\log%20|V|)=O(|E|\log%20|V|))
 + Fibonacci heap and adjacency list	![equation](http://latex.codecogs.com/gif.latex?O(|E|+|V|\log%20|V|)) <br>
 <a href="#head">`Back to Top`</a>

### 4.6 - Kruskal Algorithm and Clustering Problem
* Useful [Link](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) <br>
Prim's algorithm is another greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. Insead of maintaining a tree like Prim, it maintains forest.

![kruskal][kruskal1]

[kruskal1]: ./images/Kruskal.gif

<strong>Key idea</strong> <br>
Very similar to SCC, we can early stop the alogrithm to control number of classes in our graph, which is to say we can cluster the graph.

<strong>Properties</strong> <br>

* Running time O(ElogV) <br>
<a href="#head">`Back to Top`</a>

## 5.0 - Dynamic Programming
In this section, I'm going to introducce dynamic algorithms, one powerful algorithm design strategy. <br>
From [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming), dynamic programming (also known as dynamic optimization) is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions.

### 5.1 - Rod Cutting
* Useful [Link](https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/) <br>
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. <br>
The following table shows the relationship between price and length.

![len_price][len_price1]

[len_price1]: ./images/len_price.png

So, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6).

<strong>Key idea</strong> <br>
We view a decomposition as consisting of a first piece of length i cut off the left-hand end, and then a right-hand remainder of length n - i. ![equation](http://latex.codecogs.com/gif.latex?r_n%20=%20max_{1%3C=i%3C=n}(p_i%20+%20p_{n-i}))
So, the pseudocode looks like:

![rod_code][rod_code1]

[rod_code1]: ./images/rod_co.png

The recursion tree showing recursive calls resulting from a call CUT_ROD(p, n) looks like:

![rod_tree][rod_tree1]

[rod_tree1]: ./images/rod_tree.png

In order to save the repeated computation for small sub-problems, we memorized an array to store these values.

<strong>Properties</strong> <br>
* Time Complexity of the above implementation is O(n^2)  <br>
<a href="#head">`Back to Top`</a>

### 5.2 - Matrix Chain Multiplication
* Useful [Link](https://en.wikipedia.org/wiki/Matrix_chain_multiplication) <br>
Matrix chain multiplication (or Matrix Chain Ordering Problem, MCOP) is an optimization problem that can be solved using dynamic programming. Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices. The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications involved.

![matrix_mul][matrix_mul1]

[matrix_mul1]: ./images/matrix_mul.png

<strong>Key idea</strong> <br>
Optimal structure:

![mul_opt][mul_opt1]

[mul_opt1]: ./images/mul_opt.png

<strong>Properties</strong> <br>
* Time Complexity of the above implementation is ![equation](http://latex.codecogs.com/gif.latex?\Omega(n^3))  <br>
<a href="#head">`Back to Top`</a>

### 5.3 - Longest Common Subsequence
* Useful [Link](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) <br>
The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences).

<strong>Key idea</strong> <br>
From CLRS, the optimal structure for this problem is:

![long_op][long_op1]

[long_op1]: ./images/long_op.png

<strong>Properties</strong> <br>
* Time Complexity of the above implementation is $\theta(mn)$ <br>
<a href="#head">`Back to Top`</a>

### 5.4 - Floyd-Warshall Algorithm
* Useful [Link](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) <br>
Floyd–Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles).

<strong>Key idea</strong> <br>
This algorithm is based on very intuitive observation. Suppose we have a subset {1, 2, 3, 4, ..., k} (denote as V(k)) of original vertices group {1, 2, 3, ..., n}. If p is a shortest path from i to j in V(k), we have two cases. First, if k is not in p, then p must be a shortest path in V(k-1). Second, if k is in p, then we can seperate the path into two, P1: i~k, P2:k~j. and P1 must be the shortest path from i to k with V(k-1), P2 must be the shortest path from k to j with V(k-1).

![Floyd-Warshall_example][Floyd-Warshall_example1]

[Floyd-Warshall_example1]: ./images/Floyd-Warshall_example.png

<strong>Properties</strong> <br>
* Time Complexity of the above implementation is ![equation](http://latex.codecogs.com/gif.latex?\theta(V^3)) <br>
<a href="#head">`Back to Top`</a>

## 6.0 - Approximation Algorithms for NPC
From From [Wikipedia](https://en.wikipedia.org/wiki/NP-completeness), an NP-complete decision problem is one belonging to both the NP and the NP-hard complexity classes. In this context, NP stands for "nondeterministic polynomial time". The set of NP-complete problems is often denoted by NP-C or NPC. <br>

In this section, I am going to introduce three very famous NPC problems and explain approximation algorithms to approach them.

### 6.1 - Vertex Cover
* Useful [Link](https://en.wikipedia.org/wiki/Vertex_cover) <br>
A vertex cover (sometimes node cover) of a graph is a set of vertices such that each edge of the graph is incident to at least one vertex of the set. The figure below shows a minimum vertex cover (where the cover set must have at least two vertice, zero and one wouldn't help).

![cover][cover1]

[cover1]: ./images/cover.png

<strong>Key idea</strong> <br>
It is very difficult to find a minimum vertex cover but we can find a approximate cover with at most twice the vertices in polynomial time.

![cover_app][cover_app1]

[cover_app1]: ./images/cover_app.png

<strong>Properties</strong> <br>
* APPROR-VERTEX-COVER is a polynomial-time 2-approximation algorithm. <br>
<a href="#head">`Back to Top`</a>

### 6.2 - Travelling Salesman Problem
* Useful [Link](https://en.wikipedia.org/wiki/Travelling_salesman_problem) <br>
The travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" The gif shows brute force for tsp.

![bruce][bruce1]

[bruce1]: ./images/Bruteforce.gif

<strong>Key idea</strong> <br>
The approximation algorithm for tsp is a greedy algorithm (CLRS P1114). Here, I also want to introduce an <strong>exact algorithm</strong> for tsp using dynamic programming.

Subproblem: for every destination j ∈ {1,2,...,n}, every subset S ⊆ {1,2,...,n} that contains 1 and j, let L S,j = minimum length of a path from 1 to j that visits precisely the vertices of S [exactly once each].
So, Corresponding recurrence:

![exact_tsp][exact_tsp1]

[exact_tsp1]: ./images/tsp_exact.png

<strong>Properties</strong> <br>
* Running Time for exact algorithm: ![equation](http://latex.codecogs.com/gif.latex?O(%20n%202^n%20)%20O(n)%20=O(n^2%202^n%20))  <br>
<a href="#head">`Back to Top`</a>

### 6.3 - Boolean Satisfiability Problem
* Useful [Link](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) <br>
Boolean satisfiability problem (sometimes called propositional satisfiability problem and abbreviated as SATISFIABILITY or SAT) is the problem of determining if there exists an interpretation that satisfies a given Boolean formula.

3-SAT is one of Karp's 21 NP-complete problems, and it is used as a starting point for proving that other problems are also NP-hard. <br>

Herein, I introduce Papadimitriou’s Algorithm for 2-SAT (This is a <strong> very very very interesting algorithm </strong>, so I decide to introduce it even though 2-SAT is not NPC). <br>

<strong>Key idea</strong> <br>
Choose random initial assignment and pick arbitrary unsatisfied clause and flip the value of one of its variable.
Here is the pseudocode:

![2sat][2sat1]

[2sat1]: ./images/2sat.png

Such a casual dealing with clauses would suprisingly give us a very large probability to find the real answer. The mechanism lies in a physics term ([random walk](https://en.wikipedia.org/wiki/Random_walk)). If you are interested, I strongly recommend you to go through how random walk related to Papadimitriou.<br>

<strong>Properties</strong> <br>
* For a satisfiable 2-SAT instance with n variables, Papadimitriou’s algorithm produces a satisfying assignment with probability ≥ 1 − 1/n
* Runs in polynomial time
*  Always correct on unsatisfiable instances <br>
<a href="#head">`Back to Top`</a>
