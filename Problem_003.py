"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bitmap = [-1]*256
        slen = 0
        count = fin = 0
        j =0
        new_start = 0
        while(j<len(s)):
            if bitmap[ord(s[j])] != -1 and bitmap[ord(s[j])] >=new_start:
                fin = max(fin,count)
                count = j - bitmap[ord(s[j])]
                new_start = bitmap[ord(s[j])] + 1
                bitmap[ord(s[j])] = j

            else:
                count += 1
                bitmap[ord(s[j])] = j
            j+=1
        return max(fin,count)
