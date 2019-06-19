"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if  not l2:
            return l1
        cur_l1 = l1
        cur_l2 = l2
        carry = 0
        while cur_l1 and cur_l2:
            prev_l1 =cur_l1
            prev_l2 = cur_l2
            cur_l1.val = cur_l1.val + cur_l2.val + carry
            carry = int(cur_l1.val/10)
            cur_l1.val %= 10
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
        if cur_l1:
            while cur_l1:
                prev_l1 = cur_l1
                cur_l1.val += carry
                carry = int(cur_l1.val/10)
                cur_l1.val %= 10
                cur_l1=cur_l1.next
        elif cur_l2:
            prev_l1.next = cur_l2
            while cur_l2:
                prev_l1 = cur_l2
                cur_l2.val += carry
                carry = int(cur_l2.val/10)
                cur_l2.val %= 10
                cur_l2=cur_l2.next

        if carry:
            prev_l1.next = ListNode(carry)
        return l1




