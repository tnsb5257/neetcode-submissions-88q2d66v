class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            if(mp.find(-nums[i]+target)!=mp.end()){
                return {mp[-nums[i]+target],i};
            }
            mp[nums[i]]=i;
        }
        return {};
    }
};