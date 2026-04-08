class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)return 0;
        unordered_set<int> st;
        int temp=1;
        int maxi=1;
        for(int n : nums)st.insert(n);
        for(int a: st){
            if(st.count(a-1))continue;
            else{
                a++;
                while(st.count(a)){
                    temp++;
                    a++; 
                }
                maxi=maxi>temp?maxi:temp;
                temp=1;
            }
        }
        return maxi;
    }
};