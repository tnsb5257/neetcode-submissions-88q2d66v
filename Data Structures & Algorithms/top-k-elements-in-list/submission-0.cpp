class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> hash;

        for(int i=0; i<n;i++){
            hash[nums[i]]++;
        }
        vector<int> arr[n+1];
        for(auto& it: hash){
            arr[it.second].push_back(it.first);
        }
        vector<int> ans;
        int cnt=0;
        for(int i=n; i>=1; i--){
            for(int x : arr[i]){
                ans.push_back(x);
                cnt++;
                if(cnt==k)return ans;
            }
        }
        return ans;
    }
};
