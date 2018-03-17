# algorithms-in-python
In this respository, I implemented some famous alogritms using python. I arrange them according to the strategy they use. And for every algorithn, I will explain the problem they try to solve and some relevant resourses.
## 1.0 Divide and Conquer
### Interger Multiplication Problem [Link](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
![Interger_MUL][picture]

[picture]: ./images/integer_mult.png
The standard procedure for multiplication of two n-digit numbers requires a number of elementary operations proportional to ${\displaystyle O(n^{2})}$. As for The Karatsuba algorithm, it reduces the running time to at most ${\displaystyle n^{\log _{2}3}\approx n^{1.585}}$ <br>

<strong>Key idea</strong> <br>
The basic step of Karatsuba's algorithm is a formula that allows one to compute the product of two large numbers ${\displaystyle x}$ and ${\displaystyle y}$ using three multiplications of smaller numbers, each with about half as many digits as ${\displaystyle x}$ or ${\displaystyle y}$, plus some additions and digit shifts. <br>
<strong>Propeties</strong> <br>
* Running Time: $T(n)=\Theta (n^{\log _{2}3})\,\!$
### 
