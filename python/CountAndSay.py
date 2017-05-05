# problem : https://leetcode.com/problems/count-and-say/#/description

class Solution(object):
    def get_seq_str(self, seq_str):
        num_cnt_list = []
        cur_str = None
        cur_cnt = 0
        for c in seq_str:
            if c != cur_str:
                if cur_str is not None:
                    num_cnt_list.append(str(cur_cnt))
                    num_cnt_list.append(cur_str)
                cur_cnt = 1
                cur_str = c
            else:
                cur_cnt += 1
        if cur_cnt:
            num_cnt_list.append(str(cur_cnt))
            num_cnt_list.append(cur_str)
        seq_str = "".join(num_cnt_list)
        return seq_str

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq_str = "1"
        for i in xrange(n - 1):
            seq_str = self.get_seq_str(seq_str)
        return seq_str