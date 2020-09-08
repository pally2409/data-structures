# Backtracking

Backtracking refers to an approach towards solving problems in an incremental manner such that we follow on a path, backtrack once we find that the path does not satisfy our constraints and incrementally solve the problem.

A backtracking problem can be either of the three types:

1. Decision problem: Find any solution
2. Optimization problem: Find the best solution
3. Enumeration problem: Find all possible solutions

## List of Problems

| Problem                                        | Link |
|------------------------------------------------|------|
| [Palindrome Partitioning](#palindrome-partitioning)               | [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)|

## Walkthrough

###Palindrome Partitioning

[LeetCode](https://leetcode.com/problems/palindrome-partitioning/)

The problem requires us to find all possible partitions of the given string such that every substring is a palindrome. Given keyword "all", we know that this is an enumeration problem. Since single characters form a palindrome themselves, we do not need to backtrack to the beginning of the solution and simply return once we have exhausted the number of possible partitions on that path. 
A very helpful discussion for this question can be found [here](https://leetcode.com/problems/palindrome-partitioning/discuss/182307/Java%3A-Backtracking-Template-General-Approach).

First we simply check if our string is empty to rule out any edge cases.

```python
if s == None or len(s) == 0:
  return []
```

We have created a recursive helper function that takes in the string, the current partition array and the final result array to be returned. Inside our helper function, we first check that if the string to be checked is empty, then we have exhausted our string and the array holding the partitions must be appended to our result.
```python
if s == None or len(s) == 0:
  result.append(list(current))
```
Then we come to the meat of the function where all the magic happens, we run a for loop for our string, we increase the range of our substring and check if it is a palindrome, if not, we simply add the next character to the substring. However, if it is a palindrome, we add it to our current partition and call our helper function on the remaining string. Once we return back to the current stack call, we remove the last added substring and continue in our for loop. 

Essentially, we choose a path, explore it, and then unchoose. 
```python
for i in range(1, len(s)+1, 1):
  temp = s[:i]
  if(self.checkPalindrome(temp)==True):
    current.append(temp)
    self.helper(s[i:], current, result)
    current.pop()
```
Our function for checking the palindrome is a simply two pointer iteration. We simply iterate forwards and backwards to check if the elements at corresponding position are equal. If not, return false. 

Our final solution looks like this:
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == None or len(s) == 0:
            return []
        result = []
        self.helper(s, [], result)
        return result
    
    
    def helper(self, s, current, result):
        if s == None or len(s) == 0:
            result.append(list(current))
            return
        else:
            for i in range(1, len(s)+1, 1):
                temp = s[:i]
                if(self.checkPalindrome(temp)==True):
                    current.append(temp)
                    self.helper(s[i:], current, result)
                    current.pop()
            return
              
    def checkPalindrome(self, s):
        i = 0
        j = len(s)-1
        while(i <= j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
```

Here's a walkthrough on an example. Suppose we have been given the example "abcdada"
We call our helper function on the entire string, we run a for loop on the entirety of the string length, 

1. We first see if s[0:1] = "a" is a palindrome, it is, so we add it to our current array. We then call our helper function on "bcdada". 
2. Inside the next recursive call, we again check if s[0:1] = "b" is a palindrome. This recursive call happens till we reach the end of our string and we have our first partition array ['a', 'b', 'c', 'd', 'a', 'd', 'a'] added to our result. 
3. Suppose we return to when the string in the helper function is 'dada'. Since we have added d to our current array and then unchose it, we now check whether 'da' is a palindrome, its not. We again check whether 'dad' is a palindrome, it is!. So it is added to our current array and the helper function is called for 'a'. So our current array partition results in ['a', 'b', 'c', 'dad', 'a'].



