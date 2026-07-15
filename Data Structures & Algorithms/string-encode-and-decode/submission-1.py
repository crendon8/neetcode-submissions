class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            len_str = ''
            while s[i] != "#":
                len_str += s[i]
                i+=1
            i+=1
            astr = ''
            for j in range(int(len_str)):
                astr += s[i]
                i+=1
            res.append(astr)
            # print(res)

        return res
