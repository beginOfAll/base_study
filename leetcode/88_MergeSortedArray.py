class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: list[int]
        :type m: int
        :type nums2: list[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        temp = {}
        count = 0
        if m == 0:
            temp = {k: v for k, v in enumerate(nums2)}
        else:
            for n2 in nums2:
                if n2 < nums1[0]:
                    temp[0] = n2
                elif n2 >= nums1[m - 1]:
                    temp[m] = n2
                else:
                    for k in range(m):
                        if n2 >= nums1[k] and n2 < nums1[k + 1]:
                            temp[k + 1] = n2
        for index in temp:
            nums1.insert(index + count, temp[index])
            count += 1


s = Solution()
num1 = [1]
num2 = []
s.merge(num1, 1, num2, 0)
print(num1)
###
# leetcode 测试集有错
