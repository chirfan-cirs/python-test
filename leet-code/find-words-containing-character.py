class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
"""
:type words: List[str]
:type x: str
:rtype: List[int]
"""
