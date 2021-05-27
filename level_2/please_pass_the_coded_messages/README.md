## Please Pass the Coded Messages

Time to solve: 168 hours = 7 days.

### Description

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

### Languages

To provide a Python solution, edit solution.py

To provide a Java solution, edit solution.java

### Test Cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
#### Test Case 1

Input:

```
Solution.solution({3, 1, 4, 1})
```

Output:

```
4311
```
#### Test Case 2

Input:
```
Solution.solution({3, 1, 4, 1, 5, 9})
```
Output:

```
94311
```
-- Python cases --
#### Test Case 1

Input:
```
solution.solution([3, 1, 4, 1])
```
Output:
```
4311
```
#### Test Case 2

Input:
```
solution.solution([3, 1, 4, 1, 5, 9])
```
Output:
```
94311
```
### Constraints
#### Java
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

#### Python
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.