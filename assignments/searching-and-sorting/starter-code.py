"""Starter code for the Searching and Sorting Algorithms assignment."""


def linear_search(values: list[int], target: int) -> int:
    """Return the first index containing target, or -1 if it is missing."""
    # TODO: Check each value from left to right.
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    """Return target's index in sorted_values, or -1 if it is missing."""
    # TODO: Use left and right boundaries to narrow the search range.
    return -1


def insertion_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values without changing the input list."""
    # TODO: Copy the input and insert each value into its sorted position.
    return []


numbers = [14, 3, 9, 3, 18, 7]
sorted_numbers = [3, 3, 7, 9, 14, 18]

print("Linear search:", linear_search(numbers, 9))
print("Binary search:", binary_search(sorted_numbers, 14))
custom_sorted = insertion_sort(numbers)
print("Insertion sort:", custom_sorted)
print("Matches sorted():", custom_sorted == sorted(numbers))
