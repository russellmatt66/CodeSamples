# I wrote this
def card_value(card, total):
    if (card == 'K' or card == 'J' or card == 'Q'):
        return 10
    elif (card == 'A'):
        if total + 11 < 21:
            return 11
        else: 
            return 1
    else:
        return int(card)

# I wrote this
# Put all the aces in the back of the hand so that card_value works correctly 
def sort_aces(hand):
    computeHand = []
    numAces = 0
    for card in hand:
        if (card == 'A'):
            numAces += 1
            continue
        else:
            computeHand.append(card)
    
    for a in range(numAces):
        computeHand.append('A')
    
    return computeHand

# I wrote this
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total1 = 0
    total2 = 0
    
    computeHand1 = sort_aces(hand_1)
    computeHand2 = sort_aces(hand_2)
    
    # Need to pre-sort hands so that Aces all appear at the end
    for card in computeHand1:
        total1 += card_value(card, total1)
        
    for card in computeHand2:
        total2 += card_value(card, total1)
    
    if (total1 > 21): return False
    if (total2 > 21): return True
    if (total1 > total2): return True
    return False
    

# Kaggle specific
# Check your answer
# q3.check()
