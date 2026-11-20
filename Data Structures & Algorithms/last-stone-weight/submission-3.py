class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)

        while len(stone) > 1:
            x = heapq.heappop(stone)
            y = heapq.heappop(stone)

            if x < y:
                heapq.heappush(stone, (x- y))
        
        stone.append(0)
        return abs(stone[0])
