class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n+1,1),post(n+1,1);
        for(int i =1; i<n+1;i++){
            pre[i]=pre[i-1]*nums[i-1];
        }
        for(int i =n-1; i>=1;i--){
            post[i]=post[i+1]*nums[i];
        }
        vector<int>ans;
        for(int i=0; i<n; i++){
            ans.push_back(pre[i]*post[i+1]);
        }
        return ans;
    }
};