class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int, int>> v;

        for(int i=0; i<n; i++) {
            v.push_back({nums[i], i});
        }

        sort(v.begin(), v.end());

        for(int i=0, j=n-1; i<j;) {
            if (v[i].first + v[j].first == target) {
                vector<int> t;
                t.push_back(v[i].second);
                t.push_back(v[j].second);
                sort(t.begin(), t.end());
                return t;
            } else if (v[i].first + v[j].first > target) {
                j--;
            } else {
                i++;
            }
        }

        return {-1, -1};
    }
};
