# I wrote this using word_search() and satisfies_requirements() from "word_search.py" 
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    return_dict = dict()
    for k in range(len(keywords)):
        kw = keywords[k]
        return_dict[kw] = word_search(doc_list, kw)
    
    return return_dict

# Check your answer
# q3.check()
