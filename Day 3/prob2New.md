
Raman attended GRASP workshop and learned about binary search a month ago. After that, 
 chef implemented binary search but forgot to 
sort array.chef later realized that binary search algorithm may not work.since chef does not know how to sort array, he want to solve this problem the other way around.he wants to know the number of swaps required to get correct answer for given element.can you help chef to solve this problem?


you will be given an unsorted array A and and Q queries. In each query, you will be given an integer X. you need to determine number of swaps in  array A required to get correct answer by binary search.

 
### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$ denoting the number of elements in the array and the number of students.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.
- The following $Q$ lines describe queries. Each of these lines contains a single integer $X$.

### Output
For each query, print a single line containing one integer — the minimum required number of swaps, or $-1$ if it is impossible to make the algorithm find the correct answer. (Do you really think Chef can fail?)

### Constraints 
- $1 \le T \le 10$
- $1 \le N, Q \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- $1 \le X \le 10^9$
- all elements of $A$ are pairwise distinct
- for each query, $X$ is present in $A$
- sum of $N$ over all test cases $\le 5\cdot10^5$
- sum of $Q$ over all test cases $\le 5\cdot10^5$

### Subtasks
**Subtask #1 (20 points):** $1 \le N \le 10$

**Subtask #2 (30 points):**
- $1 \le A_i \le 10^6$ for each valid $i$
- $1 \le X \le 10^6$

**Subtask #3 (50 points):** original constraints

### Example Input
```
1
7 7
3 1 6 7 2 5 4
1
2
3
4
5
6
7
```

### Example Output
```
0
1
1
2
1
0
0
```

### Explanation
**Example case 1:**
- Query 1: The algorithm works without any swaps.
- Query 2: One solution is to swap $A_2$ and $A_4$.
- Query 3: One solution is to swap $A_2$ and $A_6$.
- Query 4: One solution is to swap $A_2$ with $A_4$ and $A_5$ with $A_6$.
- Query 5: One solution is to swap $A_2$ and $A_4$.
- Query 6: The algorithm works without any swaps.
- Query 7: The algorithm works without any swaps.
