class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
res = s.twoSum(nums, 7)
print(res)
## 从list内返回 两数之和是目标数的下标
