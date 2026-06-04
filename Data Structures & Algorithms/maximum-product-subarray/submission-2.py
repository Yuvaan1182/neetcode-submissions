class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mxP = 1
        mnP = 1
        mx = max(nums)

        for num in nums:
            if num == 0:
                mxP = 1
                mnP = 1
                mx = max(mx, num)
                continue
            tempMx = num * mxP
            mxP = max(mnP * num, tempMx, num)
            mnP = min(mnP * num, tempMx, num)
            mx = max(mxP, mx)
        return mx