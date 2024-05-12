import pandas as pd

def parseBaseStats(char_bases: str, data_dict: dict, features: list) -> None:
    print(len(features))
    print(len(char_bases))
    i = 0
    for feature in features:
        # print(char_bases[i])
        data_dict[feature].append(char_bases[i])
        i += 1
    return

char_base_dict = {}

with open('vanilla_bases.txt', 'r') as bfile:
    first_line = bfile.readline().strip('\n').split('\t')
    features = first_line[:-2]
    
    for feature in features:
        # feature = feature.strip()
        char_base_dict[feature] = []
        # print(feature)
    print(features)
    
    for line in bfile:
        # print(line)
        char_bases = line.split("\t")
        # print(char_bases)
        # char_bases.strip('\t')
        parseBaseStats(char_bases, char_base_dict, features)

base_df = pd.DataFrame(char_base_dict)

print(base_df.head())

base_df.to_csv('vanilla_bases.csv', index=False)

