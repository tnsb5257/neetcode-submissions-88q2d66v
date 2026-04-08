class Solution {
public:
    bool isPalindrome(string s) {
        string m;
        for(char c: s){
            if(isalnum(c)){
                m+=tolower(c);
            }
        }
        int left =0;
        int right = m.length()-1;
        while(left<=right){
            if(m[left]==m[right]){
                left++;
                right--;
            }else{
                return false;
            }
        }
        return true;
    }
};
