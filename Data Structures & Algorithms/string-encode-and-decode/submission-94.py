class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += f"{len(s)}#{s}"
        # print(en)
        return en

    def decode(self, s: str) -> List[str]:
        remaining = s
        res = []
        while remaining:
            slen, rest = remaining.split("#", 1)
            slen = int(slen)
            res.append(rest[0:slen])
            remaining = rest[slen:]
        return res