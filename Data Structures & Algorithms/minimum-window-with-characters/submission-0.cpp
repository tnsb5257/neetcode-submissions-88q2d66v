class Solution {
public:
    string minWindow(string s, string t) {
        int formed=0,needed=0, m=s.size(),n=t.size(),l=0,mini=INT_MAX,a=0;
        if(n>m)return "";
        vector<int> need(128,0),win(128,0);
        for(char c:t) need[c]++;
        for(auto it: need){
            if(it>0) needed++;
        }
        for(int r=0; r<m;r++){
            win[s[r]]++;
            if(need[s[r]]>0 && need[s[r]]==win[s[r]]) formed++;

            while(formed==needed){
                if((r-l+1)<mini){
                    mini=r-l+1;
                    a=l;
                }

                char leftchar = s[l];
                win[leftchar]--;
                if(need[leftchar]>0 && need[leftchar]>win[leftchar])formed--;
                l++;
            }
        }
        if(mini>m)return "";
        return s.substr(a,mini);
    }
};