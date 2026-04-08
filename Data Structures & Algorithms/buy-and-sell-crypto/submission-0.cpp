class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int maxi=0,mini=INT_MAX;
        for(int i=0; i<n; i++){
            if(prices[i]<mini){
                mini=prices[i];
                continue;
            }else{
                maxi=max(maxi,prices[i]-mini);
            }
        }
        return maxi;
    }
};