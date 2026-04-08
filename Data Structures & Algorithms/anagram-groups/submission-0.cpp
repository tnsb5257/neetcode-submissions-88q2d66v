class Solution {
public:
    string sortString(string str)
{
    string ans;
    int charCount[26] = {0};
     
    for (int i=0; i<str.length(); i++){
        charCount[str[i]-'a']++; 
    }
    
    for (int i=0;i<26;i++){
        for (int j=0;j<charCount[i];j++){
            ans+= (char)('a'+i);
        }
    }
    return ans;
}

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> ans;

        for(auto& x : strs){
            string s = sortString(x);
            ans[s].push_back(x);
        }

        vector<vector<string>> res;

        for(auto& pair : ans){
            res.push_back(pair.second);
        }
        return res;
    }
};
