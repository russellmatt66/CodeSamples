// https://leetcode.com/problems/number-of-1-bits/submissions/?envType=daily-question&envId=2023-11-29
// 0 ms (100%)
// 6.59 MB (9.00%)
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int num_ones = 0, shifted_out_bit;
        while (n){
            shifted_out_bit = n & 1;
            if (shifted_out_bit){
                num_ones += 1;
            }
            n >>= 1;
        }
        return num_ones;
    }
};