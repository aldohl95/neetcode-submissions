class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            seen[num] = 1 + seen.get(num, 0);
        for key, value in seen.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1,0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
