class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string word_merged;
        int min_len;
        (word1.size() > word2.size()) ? min_len = word2.size() : min_len = word1.size();
        for (int iw = 0; iw < min_len; iw++) {
            word_merged.push_back(word1[iw]);
            word_merged.push_back(word2[iw]);
        }
        int temp;
        if (min_len == word1.size()){ // finish appending rest of word2
            temp = word1.size();
            while (temp < word2.size()){
                word_merged.push_back(word2[temp]);
                temp += 1;
            }
        }
        else if (min_len == word2.size()){
            temp = word2.size();
            while (temp < word1.size()){
                word_merged.push_back(word1[temp]);
                temp += 1;
            }
        }
        return word_merged;
    }
};