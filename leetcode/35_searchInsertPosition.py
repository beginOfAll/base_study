class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return length
        for i in range(length):
            if nums[i] == target:
                return i
            if nums[i] < target:
                if nums[i + 1] > target:
                    return i + 1
