# problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_cnt = 0
        max_cnt = 0
        for idx, c in enumerate(s):
            find_idx = s.find(c, idx-cur_cnt, idx)
            if find_idx < 0:
                cur_cnt += 1
            else:
                cur_cnt = idx - find_idx
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt
        return max_cnt