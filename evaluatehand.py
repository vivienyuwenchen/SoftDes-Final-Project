"""
take a list of tuples (value, suit)
"""
# what is the docstring above applying to? It's a module comment, but
# I believe it's meant to describe a particular function.


def straightscore(hand):
    values = []
    for card in hand:
        values.append(int(card[0]))
    values = list(set(values))
    # above could also be written:
    #   values = sorted({int(card[0] for card in hand)}, reverse=True)
    # I also wonder whether card[0] should have been converted to an int
    # upstream from here, though.
    if len(values) >= 5:
        values.sort(reverse=True)
        for i in range(len(values) - 4):
            if values[i] == values[i + 4] + 4:
                # rank of a straight is fully defined by high card
                # document this use of 4e10. Better, use a constant.
                # Best: use a tuple instead. tuples sort the way you
                # want them to. For example:
                #  return STRAIGHT, values[i]
                # where STRAIGHT holds a value that sorts correctly with
                # the value of Flush, etc.
                return 4e10 + values[i]
    return 0


def flushscore(hand):
    suit_count = {}
    for card in hand:
        if card[1] in suit_count:
            suit_count[card[1]] += 1
        else:
            suit_count[card[1]] = 1
    for suit in suit_count:
        if suit_count[suit] >= 5:
            values = []
            for card in hand:
                if card[1] == suit:
                    values.append(card[0])
                    values.sort(reverse=True)
                    # check for a strait flush
                    for i in range(len(values) - 4):
                        if values[i] == values[i + 4] + 4:
                            # rank of a strait is fully defined by high card
                            return 8e10 + values[i]
            # need to account for all 5 cards in flush
            score = 5e10
            for i in range(0, 5):
                score += values[i] * 10**(8 - 2 * i)
            return score
    return 0


def pairscore(hand):
    cards = []
    for n in hand:
        cards.append(n[0])
    values = list(set(cards))
    pair = []
    for n in values:
        pair.append((cards.count(n), n))
    pair.sort(reverse=True)
    # or:
    #   values = list({n[0] for n in hand})
    #   pairs = [cards.count(n), n) for n in values]
    #
    # The following would be easier to read with use of classes or namedtuple
    # replace …[0] by something more mnemonic.
    if pair[0][0] == 4:
        # four of a kind
        return 7e10 + pair[0][1] * 1e8)  # this is sufficient for 4oa
    elif pair[0][0] == 3:
        if pair[1][0] >= 2:
            # full house
            return 6e10 + pair[0][1] * 1e8 + pair[1][1] * 1e6
        # three of a kind
        else:
            score=3e10 + pair[0][1] * 10e8
            for i in range(1, len(values)):
                score += values[i] * 10**(6 - 2 * i)
            return score
    elif pair[0][0] == 2:
        if pair[1][0] == 2:
            # two pair
            return 2e10 + pair[0][1] * 10e8 + pair[1][1] * 10e6 + pair[2][1]
        # one pair
        else:
            score=1e10
            for i in range(0, len(values)):
                score += pair[i][1] * (10**(8 - 2 * i))
            return score
    else:
        return 0


def scorehand(hand):
    "Returns an int that can be used to directly compare hands."
    scores=[straightscore(hand), flushscore(hand), pairscore(hand)]
    scores.sort(reverse = True)
    return int(scores[0])
