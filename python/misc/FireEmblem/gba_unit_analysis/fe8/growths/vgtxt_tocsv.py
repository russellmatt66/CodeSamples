import pandas as pd

def parseTxtLine(data_line: str) -> list:
    clean_data = [''] * 8
    char_data = data_line.split(' ')
    # Handle exceptions
    if (char_data[0] == 'Character' or char_data[0] == 'Name'): return []
    
    # Below can be refactored so that everything happens inside one for loop
    if (len(char_data) == 9): # Phantom Class
        clean_data[0] = char_data[0] + " " + char_data[1]
        for i in range(2, len(char_data)):
            clean_data[i-1] = char_data[i].split('\t')[1]
            if (i == 8): # also need to remove \n char
                clean_data[i-1] = clean_data[i-1].split('\n')[0]
    else:
        clean_data[0] = char_data[0] 
        for i in range(1, len(char_data)):
            print(char_data[i].split('\t'))
            clean_data[i] = char_data[i].split('\t')[1]
            if (i == 7):
                clean_data[i] = clean_data[i].split('\n')[0]
    
    print(clean_data)
    return clean_data

def addCharData(data_dict: dict, char_data: list) -> None:
    data_dict['Name'].append(char_data[0])
    data_dict['HP'].append(int(char_data[1]))
    data_dict['S/M'].append(int(char_data[2]))
    data_dict['Skl'].append(int(char_data[3]))
    data_dict['Spd'].append(int(char_data[4]))
    data_dict['Lck'].append(int(char_data[5]))
    data_dict['Def'].append(int(char_data[6]))
    data_dict['Res'].append(int(char_data[7]))
    return

chardata_dict = {}
features = ['Name', 'HP', 'S/M', 'Skl', 'Spd', 'Lck', 'Def', 'Res']

for feature in features:
    chardata_dict[feature] = []

il = 0
with open('vanilla_growths.txt', 'r') as vgf:
    for line in vgf:
        print(f"Parsing line {il}")
        char_data = parseTxtLine(line)
        il += 1
        if not char_data: continue
        else: addCharData(chardata_dict, char_data)

char_df = pd.DataFrame(chardata_dict)
char_df.to_csv('vanilla_growths.csv', index=False)
