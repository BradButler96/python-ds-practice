import collections
def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return None
    else:
        count = collections.Counter(nums)
        value = {i for i in count if count[i] == 2}
        value = value.pop()
        return value