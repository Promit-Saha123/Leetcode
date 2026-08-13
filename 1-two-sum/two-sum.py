class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        #for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]
        
        nums_dict = {}

        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for i, num in enumerate(nums):
            second = target - num

            if second in nums_dict and nums_dict[second] != i:
                return [i, nums_dict[second]]
