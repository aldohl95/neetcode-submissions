class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) -1
        res = []
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target and nums[l] == target:
                res.append(l)
                break
            elif nums[mid] == target and nums[l] < target:
                r = mid -1
                if nums[r] != target:
                    res.append(mid)
                    break
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        l, r = 0, len(nums) -1 
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target and nums[r] == target:
                res.append(r)
                break
            elif nums[mid] == target and nums[r] > target:
                l = mid + 1
                if nums[l] != target:
                    res.append(mid)
                    break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return res if res else [-1,-1]