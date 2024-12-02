# Advent of Code 2024

Overall Statistics
```
Stars Earned: 4
Part Ones Finished: 2 (12/2)
Part Twos Finished: 2 (12/2)
Days Completed: 2 (12/2)
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

## Day Two
> Language: Python

> Finished 12/2/2024 8:21 AM EST

> Finished Both Parts

### Problem Summary
**Part One**
> Given rows of data, determine if each row is safe, where a safe row is a row where each value either increases or decreases by a max of 3 from the prior value

*Solution*
> Simply check the conditionals, determine if the second value is an increase or decrease from the preceding one, then check if all values follow that same directionality, and are within 3 of the prior value

**Part Two**
> Determine how many rows are safe, if you are allowed one removed fail value per row

*Solution*
> For each row, first check if it is valid as is using the method in Part One, if it is invalid, brute force through, checking each combination of array with one value removed, if a valid one is found, return true, else false