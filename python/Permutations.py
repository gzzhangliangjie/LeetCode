# problem : https://leetcode.com/problems/permutations/#/description

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        perms = list(itertools.permutations(nums, len(nums)))
        return perms