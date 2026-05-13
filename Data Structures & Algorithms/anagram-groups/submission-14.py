from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]
        
        strsdict = defaultdict(list)
        for i, s in enumerate(strs):
            chars = list(s)
            chars.sort()
            s = "".join(chars)
            strsdict[s].append(i)

        print(strsdict)
        res = []
        for strsindexlist in strsdict.values():
            group = []
            for i in strsindexlist:
                group.append(strs[i])
            res.append(group)
        return res
        