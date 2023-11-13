// https://leetcode.com/problems/maximum-frequency-stack/submissions/
class FreqStack {
public:
    FreqStack() {
        
    }
    
    void push(int val) {
        storage_.push_back(val);
        frequency_[val]++;
    }
    
    int pop() {
        int maxFreq = 0;
        
        for (const auto& pair : frequency_){
            if (pair.second > maxFreq){
                maxFreq = pair.second;
            }
        }
        
        int popVal;
        for (int i = storage_.size()-1; i >= 0; i--){
            if (frequency_[storage_[i]] == maxFreq){
                popVal = storage_[i];
                frequency_[popVal]--;
                storage_.erase(storage_.begin() + i);
                return popVal;
            }
        }
        return popVal;
    }
private:
    vector<int> storage_;
    map<int, int> frequency_;
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */