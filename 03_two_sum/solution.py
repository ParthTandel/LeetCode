class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index = 0
        for i in nums:
            key = target - i
            if key in nums and index != nums.index(key):
                a_i = nums.index(key)
                if a_i > index:
                    return index, a_i
                else:
                    return a_i, index
            index = index + 1
        
s = Solution()
print s.twoSum([3,2,4], 6)