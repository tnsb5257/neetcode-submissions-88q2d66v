class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int l=0,r=n-1,maxi=(n-1)*(min(height[0],height[n-1])),w=n-1;
        while(l<r){
            if (height[l]<height[r]) l++;
            else r--;
            w--;
            maxi=max(maxi,w*min(height[l],height[r]));
        }
        return maxi;
    }
};