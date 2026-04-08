class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        vector<int> v1(126,0),v2(126,0);
        for(auto c: s1)v1[c]++;

        int l=0,m=s1.size(),n=s2.size();
        int i=0;
        while(i<(m-1)){
            v2[s2[i]]++;
            i++;
        }
        for(int r=m-1; r<n;r++){
            v2[s2[r]]++;
            if(v1==v2)return true;
            else{
                v2[s2[l]]--;
                l++;
            }
        }
        return false;
    }
};
