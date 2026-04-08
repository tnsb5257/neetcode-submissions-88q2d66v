class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n =nums.size();
        vector<int> ans;
        int p  = 1;
        ans.push_back(1);
        for(int i=0; i<n-1;i++){
            p = p*nums[i];
            ans.push_back(p);
        }
        p=1;
        for(int i =n-1; i>0;i--){
            p = p*nums[i];
            ans[i-1]=ans[i-1]*p;
        }
        return ans;
    }
};
