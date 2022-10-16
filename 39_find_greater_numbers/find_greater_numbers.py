def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    counter = 0
    if len(nums) == 0:
        return 0
    comp_nums = nums.copy()
    comp_nums.pop(0)
    nums.pop()
    for i in range(len(nums)):
        for j in range(len(comp_nums)):
            if nums[i] < comp_nums[j]:
                counter += 1
        comp_nums.pop(0)
    return counter
