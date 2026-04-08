class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> mp;
        int n = s.size();
        int left = 0, max_len = 0;
        
        for (int right = 0; right < n; right++) {
            // Check if character exists in our map
            if (mp.find(s[right]) != mp.end()) {
                // If it exists, update 'left' to skip the old index
                // We use max to ensure 'left' never moves backward!
                left = max(left, mp[s[right]] + 1);
            }
            
            // Store/Update the index of the current character
            mp[s[right]] = right;
            
            // Calculate the current window size
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};