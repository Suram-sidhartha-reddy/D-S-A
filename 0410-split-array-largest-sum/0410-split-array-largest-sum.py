
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subarr = 1
            cursum = 0

            for n in nums:
                if cursum + n > largest:
                    subarr += 1
                    cursum = n
                else:
                    cursum += n

            return subarr <= k

        l, r = max(nums), sum(nums)

        while l < r:
            mid = l + (r - l) // 2

            if canSplit(mid):
                r = mid
            else:
                l = mid + 1

        return l
