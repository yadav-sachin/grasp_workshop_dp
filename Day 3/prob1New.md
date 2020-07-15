What can be more fun than playing games with your siblings during the break? (Not talking about PUBG and Dota 2 though :P)   
Bob and Alice have created their own game with the following rules:
- Given a sequence $A_1, A_2, \ldots A_N$ ; a *magic number* $a$ for Bob and a magic number $b$ for Alice.
- The players play in alternate turns. In each turn, the current player must remove a number of elements (at least one) from the sequence ,and each removed element should be a multiple of the magic number of the player.
- If there is no number left for the current player to remove, the current player loses the game.
   
The task is to predict the winner of the game if both players plays optimally.   


### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $a$ and $b$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing the string `"ALICE"` if the winner is Alice or `"BOB"` if the winner is Bob (without quotes).

### Constraints 
- $1 \le T \le 10$
- $1 \le N \le 2 \cdot 10^5$
- $1 \le a, b \le 100$
- $1 \le A_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (18 points):** $a = b$

**Subtask #2 (82 points):** original constraints

### Example Input
```
2
5 3 2
1 2 3 4 5
5 2 4
1 2 3 4 5
```

### Example Output
```
ALICE
BOB
```

### Explanation
**Example case 1:** Bob removes $3$ and the sequence becomes $[1, 2, 4, 5]$. Then, Alice removes $2$ and the sequence becomes $[1, 4, 5]$. Now, Bob is left with no moves, so Alice is the winner.
