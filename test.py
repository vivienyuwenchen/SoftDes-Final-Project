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
            print("yes")

    if len(pair_vals) != 0:
        return (True, pair_vals)
    else:
        return (False, pair_vals)

list_ = ["7C", "3D", "3S", "7H", "9D", "9C", "13H"]
print(ispair(list_))
