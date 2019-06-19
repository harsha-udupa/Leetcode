"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_i = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in dict_i.values():
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != dict_i[i]:
                    return False
        if stack ==[]:
            return True
        else:
            return False
