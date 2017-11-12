def ispair(cardvalues):
    sorted_cards = sorted(cardvalues)
    for card in sorted_cards:
        card = card[:-1]

    pair_vals = []
    for i in range(0,len(sorted_cards)-1):
        card1 = sorted_cards[i]
        card2 = sorted_cards[i+1]
        if card1[:-1] == card2[:-1]:
            pair_vals.append(card1[:-1])

    if len(pair_vals) != 0:
        return (True, pair_vals)
    else:
        return (False, pair_vals)

def isthree(cardvalues):
    check = ispair(cardvalues)
    if check[0]:
        pairs = check[1]
        if len(pairs) >= 2:
            for i in range(0, len(pairs)-1):
                if pairs[i] == pairs[i+1]:
                    return ("three", pairs[0])

def isfullhouse(cardvalues):
    three_check = isthree(cardvalues)
    if three_check:
        pairs = ispair(cardvalues)
        #remove three from pair check
        if len(pairs[1])>2:
            return ('fh', three_check[1])

list_ = ["7C", "3D", "3S", "3H", "9D", "9C", "13H"]
print(isfullhouse(list_))
