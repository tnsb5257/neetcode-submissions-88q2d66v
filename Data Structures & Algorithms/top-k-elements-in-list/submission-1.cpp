class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n =nums.size();
        vector<int> ans;
        unordered_map<int,int> mp;
        for(auto x:nums)mp[x]++;
        vector<vector<int>> freq(n+1);
        for(auto it: mp)freq[it.second].push_back(it.first);
        int a=n;
        while(k>0){
            if(!freq[a].empty()){
                for(auto it: freq[a])ans.push_back(it);
                k=k-freq[a].size();;
            }
            a--;
        }
        return ans;
    }
};