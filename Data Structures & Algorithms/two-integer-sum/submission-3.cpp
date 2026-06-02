class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> diff;

        for(int i=0; i<n; i++) {
            if (diff.find(target - nums[i]) != diff.end()) {
                return { diff[target - nums[i]], i };
            }

            diff[nums[i]] = i;
        }

        return { -1, -1 };
    }
};
