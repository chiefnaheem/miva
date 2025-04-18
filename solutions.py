# solution.py

from typing import List

def plus_one(digits: List[int]) -> List[int]:
    n = len(digits)
    
    for i in reversed(range(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If we got here, all digits were 9
    return [1] + [0] * n


def alternate_min_max(arr: List[int]) -> List[int]:
    arr.sort()
    result = []

    left = 0
    right = len(arr) - 1

    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1

    return result
