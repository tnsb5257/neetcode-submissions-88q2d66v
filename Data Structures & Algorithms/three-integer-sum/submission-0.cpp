class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        for(int i=0; i<n; i++){
            if(i!=0 && nums[i-1]==nums[i])continue;
            int l=i+1,r=n-1;
            while(l<r){
                if(nums[l]+nums[r]==(-nums[i])){
                    ans.push_back({nums[i],nums[l],nums[r]});
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1])l++;
                    while(l<r && nums[r]==nums[r+1])r--;
                }
                else if(nums[l]+nums[r]>(-nums[i]))r--;
                else l++;
            }
        }
        return ans;
    }
};