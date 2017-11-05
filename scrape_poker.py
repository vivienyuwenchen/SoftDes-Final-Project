def read_hand(hand):
    """reads information from text file for a single hand"""
    all_lines = hand.splitlines() # list of each line in hand
    seat_count = 0 # make sure hand is only two players!
    round_type = ""
    cards_on_table = []
    for l in all_lines:
        if "Stage" in l:
            stage_num = l[l.find("#")+1 : l.find(":")]
            game_type = l[l.find(":")+2 : l.find("-")]
            date = l[l.find("-")+2:]
        elif "Table" in l:
            table = l[l.find(":")+1 : l.find("(Real Money)")]
            dealer_seatnum = l[l.find("#")+1 : l.find(" is")]
        elif "in chips" in l:
            if seat_count == 0:
                player1_seatnum = l[l.find(" ")+1: l.find("-")-1]
                player1_id = l[l.find("-")+2 : l.find("(")-1]
                player1_chips = l[l.find("$"): l.find("in")-1]
                #print("Defined Player 1 ID: ", player1_id)
            elif seat_count == 1:
                player2_seatnum = l[l.find(" ")+1: l.find("-")-1]
                player2_id = l[l.find("-")+2 : l.find("(")-1]
                player2_chips = l[l.find("$"): l.find("in")-1]
                #print("Defined Player 2 ID: ", player2_id)
            else:
                print("Hand has more than two players")
                return
            seat_count += 1
        elif "Posts" in l:
            if player1_id in l:
                player1_blind_type = l[l.find("Posts")+len("Posts") : l.find("blind")]
                player1_blind_amo = l[l.find("blind")+len("blind"):]
            elif player2_id in l:
                player2_blind_type = l[l.find("Posts")+len("Posts") : l.find("blind")]
                player2_blind_amo = l[l.find("blind")+len("blind"):]
        elif "** POCKET CARDS **" in l:
            round_type = "pocket"
        elif "** FLOP **" in l:
            round_type = "flop"
            cards = l[l.find("[")+1: l.find("]")]
            cards_on_table += cards.split(" ")
        elif "** TURN **" in l:
            round_type = "turn"
            card = l[l.rfind("[")+1: l.rfind("]")]                                # only one card is ever added at a time after flop
            cards_on_table.append(card)
        elif "** RIVER **" in l:
            round_type = "river"
            card = l[l.rfind("[")+1: l.rfind("]")]
            cards_on_table.append(card)
        elif "** SHOW DOWN **" in l:
            round_type = "show down"
        elif "** SUMMARY **" in l:
            round_type = "summary"
            print("--------")
            print("Summary")
            print("--------")
        elif not round_type == "summary" and not round_type == "":              # parse through actions in each round (undefined length)
            #round.round_type = round_type
            if player1_id in l:
                if "Folds" in l:
                    pass
                    #player1.act = fold
                elif "Raises" in l:
                    #player1.act = raise
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                elif "Calls" in l:
                    #player1.act = calls
                    call_amo = l[l.rfind(" "):]
                elif "Bets" in l:
                    #player1.act = bets
                    bet_amo = l[l.rfind(" "):]
                elif "Checks" in l:
                    pass
                    #player1.act = checks
                else:
                    pass
                    # Does not show, returns, etc.
            elif player2_id in l:
                if "Folds" in l:
                    pass
                    #player2.act = fold
                elif "Raises" in l:
                    #player2.act = raise
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                elif "Calls" in l:
                    pass
                    #player2.act = calls
                    call_amo = l[l.rfind(" "):]
                elif "Bets" in l:
                    #player2.act = bets
                    bet_amo = l[l.rfind(" "):]
                elif "Checks" in l:
                    pass
                    #player2.act = checks
                else:
                    pass
                    # Does not show, returns, etc.
            else:
                print("Something went wrong. No players found in round")
        elif round_type == "summary" and not l == "":
            print(l)
        else:
            print("**", l)

    if player1_seatnum == dealer_seatnum:
        dealer = player1_id
        player1_dealer = True
        player2_dealer = False
    else:
        dealer = player2_id
        player1_dealer = False
        player2_dealer = True

    print("Table: ", cards_on_table)


def per_hand(file_name):
    """divides text file into hands"""
    with open (file_name, 'rt') as f:  # Open input file for reading of text data.
        hand = ""
        prevline = ""
        all_hands = []
        for line in f: # Store each line in a string variable "line"
            if line == "\n" and prevline == "\n" and not len(hand) == 0:
                all_hands.append(hand)
                #rint(hand)
                hand = ""
            else:
                hand = hand + line
            prevline = line

        return all_hands

if __name__ == "__main__":
    all_hands = per_hand('small-text.txt')
    for h in all_hands:
        read_hand(h)
