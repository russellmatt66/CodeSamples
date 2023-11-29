// https://leetcode.com/problems/power-of-two/submissions/
// 0 ms (100%)
// 6.48 MB (19.66%)
class Solution {
public:
    bool isPowerOfTwo(int n) {
        int shifted_out_bit, num_ones = 0;
        bool is_power = false, only_one = true;
        while (n){
            shifted_out_bit = n & 1;
            if (shifted_out_bit && only_one){
                is_power = true;
                num_ones += 1;
            }
            if (num_ones > 1){
                is_power = false;
                break;
            }
            n >>= 1;
        }
        return is_power;
    }
};