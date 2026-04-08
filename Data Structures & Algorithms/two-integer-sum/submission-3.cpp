class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int x;
        unordered_map<int,int> map;
        for(int i=0; i<n; i++){
            x = target-nums[i];
            if(map.count(x)){
                return {map[x],i};
            }else{
                map[nums[i]]=i;
            }
        }
    }
};
