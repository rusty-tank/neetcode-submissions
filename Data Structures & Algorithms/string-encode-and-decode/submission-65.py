class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""

        for s in strs:
            en += f"{len(s)}#{s}"

        return en

    def decode(self, s: str) -> List[str]:
        remaining = s
        res = []

        while remaining:

            length_str, after_hash = remaining.split("#", 1)

            length = int(length_str)

            word = after_hash[:length]

            res.append(word)

            remaining = after_hash[length:]

        return res