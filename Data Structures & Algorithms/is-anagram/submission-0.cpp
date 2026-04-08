class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int> a,b;
        for(auto c:s){
            a[c]++;
        }
        for(auto d:t){
            b[d]++;
        }
        if(a==b)return true;
        return false;
    }
};
