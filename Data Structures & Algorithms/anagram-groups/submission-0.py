from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        result = []
        for s in strs:
            s_sort = "".join(sorted(s))
            groups[s_sort].append(s)
        for k, l in groups.items():
            result.append(l)
        return result
        