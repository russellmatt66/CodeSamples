class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        res = True
        word_list = sentence.split(" ")
        i = 1
        while res and i < len(word_list):
            prev_word_len = len(word_list[i-1])
            if word_list[i - 1][prev_word_len - 1] is not word_list[i][0]: # definition of circularity
                res = False
                break
            i += 1
        
        last_char_last_word = word_list[len(word_list) - 1][len(word_list[len(word_list) - 1]) - 1] # check the periodic boundary conditions
        if word_list[0][0] is not last_char_last_word:
            res = False

        return res