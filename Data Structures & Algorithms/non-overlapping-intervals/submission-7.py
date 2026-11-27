class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        newEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= newEnd:
                newEnd = end
            else:
                res += 1
                newEnd = min(end, newEnd)
        return res