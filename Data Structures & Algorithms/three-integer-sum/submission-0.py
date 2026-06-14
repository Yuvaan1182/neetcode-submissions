class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hashset = set()
        nums.sort()

        for i in range(n-2):
            j, k = i+1, n-1

            while j < k:
                if nums[i] == -(nums[j] + nums[k]):
                    x = j
                    while (x < k and nums[i] == -(nums[x] + nums[k])):
                        t = (nums[i], nums[x], nums[k]); 
                        if t not in hashset:
                            hashset.add(t)
                        x+=1
                    y = k
                    while (j < y and nums[i] == -(nums[j] + nums[y])):
                        t = (nums[i], nums[j], nums[y]);
                        if t not in hashset:
                            hashset.add(t)
                        y-=1
                    j+=1
                    k-=1
                elif nums[i] < -(nums[j]+nums[k]):
                    j+=1
                else:
                    k-=1
                    
        res = [list(t) for t in hashset]
        return res