class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> ans;
        int x;
        unordered_map<int,int> map;
        for(int i=0; i<n; i++){
            x = target-nums[i];
            if(map.count(x)){
                ans.push_back(map[x]);
                ans.push_back(i);
                return ans;
            }else{
                map[nums[i]]=i;
            }
        }
    }
};
