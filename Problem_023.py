"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """



        def attach(head,node):
            if not head and not node:
                return None
            if not head:
                return node
            if not node:
                return head

            cur=head
            prev=None
            while node and cur:
                if node.val >= cur.val:
                    prev=cur
                    cur=cur.next
                else:
                    temp=node
                    node=node.next
                    if prev:
                        prev.next=temp
                        temp.next=cur
                        prev=prev.next
                    else:
                        temp.next=cur
                        head=temp
                        cur=head
                        #print head.val
            if node:
                prev.next=node

            return head


        if not lists:
            return None
        i=1
        head=lists[0]
        while i<len(lists):
            head=attach(head,lists[i])
            i+=1
        return head

