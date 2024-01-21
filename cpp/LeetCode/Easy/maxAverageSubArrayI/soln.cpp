class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = 0;
        double max_avg;

        for (int i = 0; i < k; i++){
            sum += nums[i];
        }

        max_avg = sum / k;

        for (int j = k; j < nums.size(); j++){
            sum += nums[j];
            sum -= nums[j-k];
            max_avg = max(max_avg, sum / k);
        }

        return max_avg;
    }
};
