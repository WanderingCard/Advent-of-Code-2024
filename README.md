# Advent of Code 2024

Overall Statistics
```
Stars Earned: 2
Part Ones Finished: 1 (12/1)
Part Twos Finished: 1 (12/1)
Days Completed: 1 (12/1)
```

## Day One
> Language: Python

> Finished 12/1/2024 10:41 PM EST

> Finished Both Parts

### Problem Summary
**Part One**
> Given an input, find the total difference between the equivalent values from two lists based on rank from least to greatest (I.E Sum of the difference of the smallest numbers, then the second smallest, then so on)

*Solution*
> Get the lists, sort them, and then sum the sorted lists by index

**Part Two**
> Find how similar the lists are, for each item in the right list, find the result of the value * how many times it occurs in the other list, and sum those products together

*Solution*
> Generate a hasmap of the second list that counts the occurances of each number in that list. For each item in the first list, multiply that value by the value associated with that key in the second list hashmap