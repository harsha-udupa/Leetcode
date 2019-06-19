"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_cur = l1
        l2_cur = l2
        if not l1:
            return l2
        if not l2:
            return l1
        prev = None
        while l1_cur and l2_cur:

            if l1_cur.val <= l2_cur.val:
                prev = l1_cur
                l1_cur = l1_cur.next
            else:
                temp = l2_cur
                l2_cur = l2_cur.next
                if prev:
                    prev.next = temp
                    temp.next = l1_cur
                else:
                    temp.next = l1_cur
                    l1 = temp
                prev = temp

        if l2_cur:
            prev.next = l2_cur

        return l1
