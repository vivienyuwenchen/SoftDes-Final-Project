from hands import *

def read_hand(hand):
    """reads information from text file for a single hand"""
    all_lines = hand.splitlines() # list of each line in hand
    seat_count = 0 # make sure hand is only two players!
    round_type = ""
    cards_on_table = []
    round_types = []
    actions = []
    pocket_status1 = []
    pocket_status2 = []
    pot = 0
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
                #print("Hand has more than two players")
                return
            seat_count += 1
        elif "Posts" in l:
            if player1_id in l:
                player1_blind_type = l[l.find("Posts")+len("Posts") : l.find("blind")]
                player1_blind_amo = l[l.find("blind")+len("blind"):]
                pot += int(player1_blind_amo[2:])
            elif player2_id in l:
                player2_blind_type = l[l.find("Posts")+len("Posts") : l.find("blind")]
                player2_blind_amo = l[l.find("blind")+len("blind"):]
                pot += int(player2_blind_amo[2:])
        elif "** POCKET CARDS **" in l:
            round_type = "pocket"
            round_types.append(round_type)
        elif "** FLOP **" in l:
            round_type = "flop"
            round_types.append(round_type)
            cards = l[l.find("[")+1: l.find("]")]
            cards_on_table += cards.split(" ")
        elif "** TURN **" in l:
            round_type = "turn"
            round_types.append(round_type)
            card = l[l.rfind("[")+1: l.rfind("]")]                               # only one card is ever added at a time after flop
            cards_on_table.append(card)
        elif "** RIVER **" in l:
            round_type = "river"
            round_types.append(round_type)
            card = l[l.rfind("[")+1: l.rfind("]")]
            cards_on_table.append(card)
        elif "** SHOW DOWN **" in l:
            round_type = "show down"
            #round_types.append(round_type)
        elif "** SUMMARY **" in l:
            round_type = "summary"
            #round_types.append(round_type)
            #print("--------")
            #print("Summary")
            #print("--------")
        elif not round_type == "summary" and not round_type == "":              # parse through actions in each round (undefined length)
            #round.round_type = round_type
            if player1_id in l:
                if "Folds" in l:
                    play1_act = "fold"
                    pass
                elif "Raises" in l:
                    play1_act = "raise "
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                    raise_amo = int(new_amo[1:])-int(old_amo[1:])
                    pot += raise_amo[1:]
                    play1_act = play1_act+str(raise_amo)
                elif "Calls" in l:
                    play1_act = "call "
                    call_amo = l[l.rfind(" "):]
                    pot += call_amo[1:]
                    play1_act = play1_act+call_amo
                elif "Bets" in l:
                    play1_act = "bet "
                    bet_amo = l[l.rfind(" "):]
                    pot +=bet_amo[1:]
                    play1_act = play1_act+bet_amo
                elif "Checks" in l:
                    play1_act = "check"
                    pass
                else:
                    pass
                    # Does not show, returns, etc.
            elif player2_id in l:
                if "folds" in l:
                    play2_act = "fold"
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Raises" in l:
                    play2_act = "raise "
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                    raise_amo = int(new_amo[1:])-int(old_amo[1:])
                    pot += raise_amo[1:]
                    play2_act = play2_act+raise_amo
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Calls" in l:
                    play2_act = "call "
                    call_amo = l[l.rfind(" "):]
                    pot += call_amo[1:]
                    play2_act = play2_act+call_amo
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Bets" in l:
                    play2_act = 'bet '
                    bet_amo = l[l.rfind(" "):]
                    pot += bet_amo[1:]
                    play2_act = play2_act+bet_amo
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Checks" in l:
                    play2_act = 'check'
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                    #player2.act = checks
                else:
                    pass
                    # Does not show, returns, etc.
            else:
                print("Something went wrong. No players found in round")
        elif round_type == "summary" and not l == "":
            #print(l)
            pass
        else:
            #print("**", l)
            pass

    #print("Table: ", cards_on_table)

    rounds = []
    ##create instances
    if player1_seatnum == dealer_seatnum:
        dealer = player1_id
        player1_dealer = True
        player2_dealer = False
    else:
        dealer = player2_id
        player1_dealer = False
        player2_dealer = True

    Player1 = Player(player1_id, player1_chips, player1_dealer, pocket_status1, player1_blind_amo)
    Player2 = Player(player2_id, player2_chips, player2_dealer, pocket_status2, player2_blind_amo)
    players = [Player1, Player2]

    for i in range(len(round_types)):
        rounds.append(Round(round_types[i], players, actions[i]))

    return rounds

    hand = Hand(rounds, dealer, stage_num, pot, table_cards, summary)
    #return hand


def per_hand(file_name):
    """divides text file into hands"""
    with open (file_name, 'rt') as f:  # Open input file for reading of text data.
        hand = ""
        prevline = ""
        all_hands = []
        for line in f: # Store each line in a string variable "line"
            if line == "\n" and prevline == "\n" and not len(hand) == 0:
                all_hands.append(hand)
                #print(hand)
                hand = ""
            else:
                hand = hand + line
            prevline = line

        return all_hands

def find_games():
    """Takes input of all hands played, classifies them into games
    """

if __name__ == "__main__":
    all_hands_text = per_hand('small-text.txt')
    all_hands = read_hand(all_hands_text[1])
    #for h in all_hands:
        #read_hand(h)
    print(all_hands)
