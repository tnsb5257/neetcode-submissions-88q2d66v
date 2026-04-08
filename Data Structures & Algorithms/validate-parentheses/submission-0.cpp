class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        if(n%2 != 0)return false;
        int l=0,r=n-1;
        vector<int> v;
        for(auto c:s){
            if(c=='('||c=='{'||c=='['){
                v.push_back(c);
                continue;
            }else{
                if(v.empty())return false;
                char x=v.back();
                if((c==')'&& x=='(')||(c=='}'&& x=='{')||(c==']'&& x=='[')){
                    v.pop_back();
                }else return false;
            }
        }
        if(!v.empty())return false;
        return true;
    }
};