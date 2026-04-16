"""Array Product Calculator.

This module provides a function to calculate the product of all elements
in an array except the element at each position.
"""

from typing import List


def calculate_products(nums: List[int]) -> List[int]:
    """Calculate products of all elements except the one at each index.

    Given a list of integers, returns a new list where each element at
    position i is the product of all original numbers except the one
    at position i. Uses a two-pass prefix/suffix approach for O(n)
    time complexity without using division.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where each element is the product of all
        other elements in the input list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.

    Examples:
        >>> calculate_products([1, 2, 3, 4])
        [24, 12, 8, 6]

        >>> calculate_products([1, 0, 3, 4])
        [0, 12, 0, 0]

        >>> calculate_products([5])
        [1]

        >>> calculate_products([])
        []

        >>> calculate_products([0, 0, 3])
        [0, 0, 0]

        >>> calculate_products([2, 3])
        [3, 2]

        >>> calculate_products([-1, 2, -3, 4])
        [-24, 12, -8, 6]
    """
    if not isinstance(nums, list):
        raise TypeError(f"Expected a list, got {type(nums).__name__}")

    for i, item in enumerate(nums):
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError(
                f"All elements must be integers, but element at index {i} "
                f"is {type(item).__name__}: {item!r}"
            )

    n = len(nums)

    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [1]

    # Initialize result array with prefix products
    result = [1] * n

    # First pass: calculate prefix products (product of all elements to the left)
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Second pass: multiply by suffix products (product of all elements to the right)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    # Run examples
    test_cases = [
        [1, 2, 3, 4],
        [1, 0, 3, 4],
        [5],
        [],
        [0, 0, 3],
        [2, 3],
        [-1, 2, -3, 4],
    ]

    for test in test_cases:
        result = calculate_products(test)
        print(f"Input: {test} -> Output: {result}")

    # Run doctests
    import doctest
    doctest.testmod(verbose=True)
