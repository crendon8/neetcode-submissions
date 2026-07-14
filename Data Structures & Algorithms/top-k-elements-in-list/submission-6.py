from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        counts_sort = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        print(f"counts_sort: {counts_sort}")
        c = 0
        for j, v in counts_sort.items():
            result.append(j)
            c+=1
            if c == k:
                break
        return result