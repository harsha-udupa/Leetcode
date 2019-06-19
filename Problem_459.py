'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.

'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new=''

        for i,j in enumerate(s):
            if i==0:
                new=j
                continue
            l=len(new)
            if i+l>len(s):
                return False
            if s[i:i+l]==new:
                if (self.isvalid(s,new)):
                    return True
                else:
                    new+=j
            else:
                new=new+j
        return False

    def isvalid(self,s,new):

        if len(s)%len(new) !=0:
            return False

        for i in range(0,len(s),len(new)):
            if s[i:i+len(new)] !=new:
                return False
        return True
