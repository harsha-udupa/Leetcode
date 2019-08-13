"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""

import collections as cl
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if len(words) == 0:
            return []
        if not s or len(s) < (len(words)*len(words[0])):
            return []
        tot_word = len(words)*len(words[0])
        wordd = cl.Counter(words)
        for i in wordd.keys():
            if i not in s:
                return []
        answer = []
        i=0
        while i <= (len(s) -(len(words)*len(words[0]))):
            visited = cl.defaultdict(int)
            for j in range(i,i+tot_word,len(words[0])):
                this_word = s[j:j+len(words[0])]

                if this_word in wordd:
                    visited[this_word] += 1
                    if visited[this_word] > wordd[this_word]:
                        break
                else:
                    break
            if visited == wordd:
                answer.append(i)
            i += 1
        return answer

    
