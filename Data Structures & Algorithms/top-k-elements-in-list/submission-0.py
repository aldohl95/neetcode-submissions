class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        sort = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1
        
        for key, value in f.items():
            sort[value].append(key)

        for i in range(len(sort)-1,-1,-1):
            if not sort[i]:
                continue
            for num in sort[i]:
                res.append(num)
                if len(res) >= k:
                    return res


            