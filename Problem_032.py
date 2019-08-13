"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:


        stack  = []

        if len(s) <2 or ')' not in s or '(' not in s:
            return 0

        max_s = 0
        index = -1
        for i,j in enumerate(s):
            if j == '(':
                stack.append((j,i))
            else:
                if stack == []:
                    index = i
                    continue
                else:
                    temp = stack.pop(-1)
                    if stack != []:
                        temp_index = stack[-1][1]
                    else:
                        temp_index = index
                    max_s = max(max_s, i-temp_index)
        return max_s

    
