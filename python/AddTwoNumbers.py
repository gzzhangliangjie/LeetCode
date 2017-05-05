# problem : https://leetcode.com/problems/add-two-numbers/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_node1 = l1
        cur_node2 = l2

        l3 = None
        pre_node = None
        cur_carry = 0
        while cur_node1 is not None or cur_node2 is not None:
            cur_sum = cur_carry
            if cur_node1 is not None:
                val1 = cur_node1.val
                cur_sum += val1
                cur_node1 = cur_node1.next
            if cur_node2 is not None:
                val2 = cur_node2.val
                cur_sum += val2
                cur_node2 = cur_node2.next
            if cur_sum >= 10:
                cur_carry = cur_sum // 10
                cur_sum %= 10
            else:
                cur_carry = 0

            cur_node3 = ListNode(cur_sum)
            cur_node3.next = None
            if pre_node:
                pre_node.next = cur_node3
            else:
                l3 = cur_node3
            pre_node = cur_node3

        if cur_carry > 0:
            cur_node3 = ListNode(cur_carry)
            if pre_node:
                pre_node.next = cur_node3
        return l3