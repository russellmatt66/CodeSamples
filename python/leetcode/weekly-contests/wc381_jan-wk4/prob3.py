class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_dict = {}
        # Create a frequency hash
        for c in word:
            if c not in freq_dict:
                freq_dict[c] = 1
            else:
                freq_dict[c] += 1

        freq_dict_min2max = dict(sorted(freq_dict.items(), key=lambda item: item[1])) # ascending
        freq_dict_max2min = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)) # descending
        

        # Map the keys
        keypad_num = 2
        keypad = {}
        for knum in range(keypad_num,10):
            keypad[knum] = []
        
        # print(keypad)
        
        for c in freq_dict_max2min:
            keypad[keypad_num].append(c)
            if (keypad_num == 9):
                keypad_num = 2
            else:
                keypad_num += 1
                
        # print(keypad)
        
        # Calculate the pushes:
        # (1) Iterate over frequency hash, and get how many times that character needs to be added
        # (2) Iterate over keypad, and get how many times that key needs to be pushed for the character to be added
        # (3) Multiply-and-Add this to an accumulator
        total_pushes = 0
        for k in keypad: # loop through the keys (list of characters)
            for i in range(len(keypad[k])): # loop through the list of characters for the given key
                total_pushes += (i + 1) * freq_dict[keypad[k][i]]
        
        # print(total_pushes)

        return total_pushes
