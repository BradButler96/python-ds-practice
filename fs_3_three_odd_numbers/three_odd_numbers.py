def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    nums_len = len(nums)
    true = 0
    false = 0
    for i in range(nums_len - 2):
        if i + 2 <= nums_len:
            sum = nums[i] + nums[i + 1] + nums[i + 2]
            if sum % 2 != 0:
                true += 1
            else: 
                false += 1
    if true > 0:
        return True
    else: 
        return False