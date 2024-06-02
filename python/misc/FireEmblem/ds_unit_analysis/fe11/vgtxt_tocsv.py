import pandas as pd

def parseTxtLine(data_line: str) -> list:
    clean_data = [''] * 10
    char_data = data_line.split(' ')
    while '' in char_data:
        char_data.remove('')
    print(char_data)
    # Handle exceptions
    if (char_data[0] == 'Character' or char_data[0] == 'Name'): return []
    
    clean_data[0] = char_data[0]
    start_idx = 1
    cl_idx = 1

    if len(char_data) == 12: # For example: Class = "Cavalier / Paladin"
        start_idx = 4
        cl_idx = 2
        clean_data[1] = char_data[1].strip('\t') + char_data[2] + char_data[3]

    if len(char_data) == 13: # For example: Class = "Dark Mage / Sorceror"
        start_idx = 5
        cl_idx = 2
        clean_data[1] = char_data[1].strip('\t') + char_data[2] + char_data[3] + char_data[4]

    for i in range(start_idx, len(char_data)):
        print(char_data[i].split('\t'))
        
        if (char_data[i].split('\t') == 2):
            clean_data[cl_idx] = char_data[i].split('\t')[1]
        else:
            clean_data[cl_idx] = char_data[i]

        if (i == len(char_data) - 1):
            # print(clean_data[cl_idx])
            clean_data[cl_idx] = clean_data[cl_idx].split('\n')[0]
        cl_idx += 1

    print(clean_data)
    return clean_data

def addCharData(data_dict: dict, char_data: list) -> None:
    data_dict['Name'].append(char_data[0])
    data_dict['Class'].append(char_data[1])
    data_dict['HP'].append(int(char_data[2]))
    data_dict['Str'].append(int(char_data[3]))
    data_dict['Mag'].append(int(char_data[4]))
    data_dict['Skl'].append(int(char_data[5]))
    data_dict['Spd'].append(int(char_data[6]))
    data_dict['Lck'].append(int(char_data[7]))
    data_dict['Def'].append(int(char_data[8]))
    data_dict['Res'].append(int(char_data[9]))
    return

chardata_dict = {}
features = ['Name', 'Class', 'HP', 'Str', 'Mag', 'Skl', 'Spd', 'Lck', 'Def', 'Res']

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
