class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        sort(strs.begin(),strs.end());
        int n=strs.size();
        string f=strs[0],l=strs[n-1];
        for(int i=0; i<min(f.size(),l.size());i++){
            if(f[i]==l[i]){
                ans+=f[i];
            }
            else return ans;
        }
        return ans;
    }
};