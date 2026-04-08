class Solution {
public:
    int trap(vector<int>& height) {
        int lmx=0,rmx=0,n=height.size();
        vector<int> lm(n,0),rm(n,0);
        for(int i=0; i<n; i++){
            lmx=max(lmx,height[i]);
            lm[i]=lmx;
        }
        for(int i=n-1;i>=0;i--){
            rmx=max(rmx,height[i]);
            rm[i]=rmx;
        }
        int vol=0;
        for(int i=0;i<n;i++){
            vol += max(min(lm[i],rm[i])-height[i],0);
        }
        return vol;
    }
};
