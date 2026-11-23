class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortInter = sorted(intervals)
        res = []

        resP = 0

        for r in range(len(sortInter)):
            if not res:
                res.append(sortInter[r])
                continue
            if sortInter[r][0] <= res[resP][1]:
                res[resP][1] = max(res[resP][1],sortInter[r][1])
            else:
                res.append(sortInter[r])
                resP += 1
        return res
            