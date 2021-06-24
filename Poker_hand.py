from collections import Counter

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":11, "Q":12, "K":13, "A":14}
hand_dict = {10: "Royal Flush", 9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"Two Pair", 2:"Pair", 1:"High Card"}

def check_royal_flush(hand):
    values = [i[:-1] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values)
    if check_straight(hand) and check_flush(hand) and (min(rank_values) == 10):
        return True
    return False
    
def check_straight_flush(hand):
    if check_straight(hand) and check_flush(hand):
        return True
    return False
    
def check_four_of_a_kind(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False
    
def check_full_house(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    suits = [i[-1] for i in hand]
    if len(set(suits)) == 1:
        return True
    return False

def check_straight(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    else:
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

def check_three_of_a_kind(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    if set(value_counts.values()) == set([1,3]):
        return True
    return False   

def check_two_pair(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    return False

def check_pair(hand):
    values = [i[:-1] for i in hand]
    value_counts = Counter(values)
    if set(value_counts.values()) == set([1,2]):
        return True
    return False

def poker_hand_ranking(hand):
    """Function that will rank your hand"""
    
    # Royal FLush
    if check_royal_flush(hand):
        return print("Royal Flush")
    if check_straight_flush(hand):
        return print("Straight Flush")
    if check_four_of_a_kind(hand):
        return print("Four of a Kind")
    if check_full_house(hand):
        return print("Full House")
    if check_flush(hand):
        return print("Flush")
    if check_straight(hand):
        return print("Straight")
    if check_three_of_a_kind(hand):
        return print("Three of a kind")
    if check_two_pair(hand):
        return print("Two Pair")
    if check_pair(hand):
        return print("Pair")
    else:
        return print("High Card")
        
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"])
poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"])
poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"])
poker_hand_ranking(["Ah","2h", "3h", "4h", "5h"])