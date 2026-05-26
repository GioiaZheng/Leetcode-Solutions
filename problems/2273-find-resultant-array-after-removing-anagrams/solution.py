class Solution:
    def removeAnagrams(self, words):
        res = [words[0]]   # always keep the first word
        
        for i in range(1, len(words)):
            # only append if not an anagram of previous kept word
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])
        
        return res
