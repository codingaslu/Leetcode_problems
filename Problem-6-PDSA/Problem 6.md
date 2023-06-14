## Live Coding Problem 6

Write a Python function `histogram(l)` that takes as input a list of integers with repetitions and returns a list of pairs as follows:.

- for each number `n` that appears in `l`, there should be exactly one pair `(n,r)` in the list returned by the function, where `r` is the number of repetitions of `n` in `l`.
- the final list should be sorted in ascending order by `r`, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

**Sample Input**

```
[13,12,11,13,14,13,7,7,13,14,12]
```

**Output**

```python
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]
```

**Sample Input**

```
[13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7]
```

**Output**

```python
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]
```


