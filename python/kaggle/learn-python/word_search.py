# I wrote this
def satisfies_requirements(doc, keyword):
    doc_proc = doc.lower()
    kw_proc = keyword.lower()
    doc_proc = doc_proc.replace('.'," ").replace(','," ")
    kw_locations = []
    index = doc_proc.find(kw_proc)
    
    # Find all instances of the keyword in the string
    while(index != -1):
        kw_locations.append(index)
        index = doc_proc.find(kw_proc, index+1)
    
    print(keyword)
    print(kw_locations)
    
    # Ensure that the keywords found at these locations are not found as part of a compound word
    for k in range(len(kw_locations)):
        kw_loc = kw_locations[k]
        print(len(doc_proc) - len(kw_proc))
        if kw_loc == 0: 
            if doc_proc[kw_loc + len(kw_proc)] != " ":
                kw_locations.pop(k)
                continue
        elif kw_loc == len(doc_proc) - len(kw_proc):
            if doc_proc[kw_loc - 1] != " ":
                kw_locations.pop(k)
                continue
        elif (doc_proc[kw_loc - 1] != " " or doc_proc[kw_loc + len(kw_proc)] != " "): # check if it stands alone
            kw_locations.pop(k)
            continue
    
    return any(kw_locations)

# I wrote this
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    return_list = []
    for i in range(len(doc_list)):
        doc = doc_list[i]
        print(doc)
        if (satisfies_requirements(doc, keyword)):
            return_list.append(i)
    return return_list

# This is from Kaggle 
# Check your answer
# q2.check()
