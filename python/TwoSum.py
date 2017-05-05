# problem : https://leetcode.com/problems/two-sum/#/description

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        this_idx = None
        other_idx = None
        for idx, num in enumerate(nums):
            other_nums = nums[idx + 1 :]
            other_num = target - num
            if other_num in other_nums:
                other_idx = other_nums.index(other_num) + idx + 1
                this_idx = idx
                break
        return [this_idx, other_idx]