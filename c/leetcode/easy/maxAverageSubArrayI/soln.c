double findMaxAverage(int* nums, int numsSize, int k) {
    double sum = 0;
    double max_avg;

    for (int i = 0; i < k; i++){
        sum += nums[i];
    }

    max_avg = sum / k;

    for (int j = k; j < numsSize; j++){
        sum += nums[j];
        sum -= nums[j - k];
        if (sum / k > max_avg){
            max_avg = sum / k;
        }
    }

    return max_avg;
}
