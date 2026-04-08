class Solution {
public:
    void merge(vector<int>& arr,int low, int mid, int high){
        vector<int> x;
        int l=low,r=mid+1;
        while(l<=mid && r<=high){
            if(arr[l]<=arr[r]){
                x.push_back(arr[l]);
                l++;
            }
            else{
                x.push_back(arr[r]);
                r++;
            }
        }
        while(l<=mid){
            x.push_back(arr[l]);
            l++;
        }
        while(r<=high){
            x.push_back(arr[r]);
            r++;
        }
        for(int i=low; i<=high; i++){
            arr[i]=x[i-low];
        }
    }
    void mergeSort(vector<int>& arr, int low, int high){
        if(low==high)return;
        int mid =(low+high)/2;
        mergeSort(arr,low,mid);
        mergeSort(arr,mid+1,high);
        merge(arr,low,mid,high);
    }

    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums,0,nums.size()-1);
        return nums;
    }
};