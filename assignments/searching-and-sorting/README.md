# 📘 Assignment: Searching and Sorting Algorithms

## 🎯 Objective

Implement common searching and sorting algorithms in Python and use them to reason about how different approaches solve the same problem. Practice writing functions, handling edge cases, and comparing algorithm behavior without relying on built-in search or sort helpers.

## 📝 Tasks

### 🛠️ Implement Linear Search

#### Description

Complete `linear_search()` so it checks a list from left to right and returns the index of the first matching value.

#### Requirements

Completed program should:

- Return the index of the first occurrence of `target` in `values`.
- Return `-1` when `target` is not present.
- Work correctly with an empty list and a list containing duplicate values.
- Avoid using `list.index()` or another built-in search helper.

### 🛠️ Implement Binary Search

#### Description

Complete `binary_search()` for a list that is already sorted in ascending order. Repeatedly narrow the search range until the target is found or no values remain.

#### Requirements

Completed program should:

- Return the index of `target` when it is present in the sorted list.
- Return `-1` when `target` is not present.
- Correctly handle an empty list, a one-item list, and targets outside the list's range.
- Use a left and right boundary to narrow the search range instead of checking every value from the beginning.

### 🛠️ Build and Compare a Sorting Algorithm

#### Description

Complete `insertion_sort()` to return the values in ascending order, then use the provided examples to compare your result with Python's `sorted()` function.

#### Requirements

Completed program should:

- Return a new sorted list without changing the original input list.
- Correctly sort empty lists, already sorted lists, reverse-ordered lists, and lists with duplicate values.
- Implement the sorting logic without calling `sorted()` or `.sort()` inside the function.
- Include a short comparison in the program output showing that the custom result matches Python's `sorted()` result.
