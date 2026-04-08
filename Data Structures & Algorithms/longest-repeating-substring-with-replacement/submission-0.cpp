class Solution {
public:
    int characterReplacement(string s, int k) {
        int n=s.size();
        int l=0,mf=0,maxi=0;
        vector<int> v(128,0);
        for(int r=0; r<n; r++){
            v[s[r]]++;
            mf=max(mf,v[s[r]]);
            if((r-l+1-mf)>k){
                v[s[l]]--;
                l++;
            }
            maxi=max(maxi,r-l+1);
        }
        return maxi;
    }
};