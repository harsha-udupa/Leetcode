"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""


class Solution:
    def convert(self, s: str, k: int) -> str:
        arr = [""]*k
        row = col = index =0
        rt = k-1
        if len(s)<3 or k==1:
            return s

        while index < len(s):

            if col%rt == 0:
                for i in range(k):
                    print (i)
                    arr[i]+=s[index]
                    row+=1
                    index += 1
                    if index == len(s):
                        break
                col+=1
            else:
                arr[rt-(col%rt)]+=s[index]
                col+=1
                index+=1
                row=0
        res =""
        for i in arr:
            res+=i
        return res
