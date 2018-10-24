class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempMax = None
        curSum = 0
        for i in nums:
            if curSum <= 0:
                curSum = i
            else:
                curSum += i
            if tempMax is None or tempMax < curSum:
                tempMax = curSum
        return tempMax

    def maxSubArray2(self, nums):
        tempMax = max(nums)
        curSum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum + i)
            tempMax = max(tempMax, curSum)
        return tempMax


l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
res = s.maxSubArray(l)
print(res)
