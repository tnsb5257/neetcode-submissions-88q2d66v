class Solution {
public:
    bool check(vector<int>& piles, int k,int h,int sum){
        int s=0;
        for(int it:piles) s+= (it%k==0 ? it/k : (it/k +1));
        if(s<=h)return true;
        else return false;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        long long sum = 0;
        int maxi=0;
        for(int it: piles){
            sum+=it;
            maxi=max(maxi,it);
        }
        int l=sum/h>=1?sum/h:1;
        int r=maxi;
        while(l<r){
            int mid = (l+r)/2;
            if(check(piles,mid,h,sum))r=mid;
            else l=mid+1;
        }
        return r;
    }
};