class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int mxP = INT_MIN;
        int sp = prices[n-1];

        for(int r=n-2; r>=0; r--) {
            if (prices[r] > sp) {
                sp = prices[r];
                continue;
            }
            if (prices[r] < sp) {
                int pr = sp - prices[r];
                mxP = max(mxP, pr);
            }
        }

        return mxP < 0 ? 0 : mxP;
    }
};

// iterate from r -> l
// sp = 1
// cp = INT_MAX

// if curr > sp
//     sp = curr 
//     continue
// if curr < sp
//     pr = sp - curr
//     mxP = max(pr, mxP)