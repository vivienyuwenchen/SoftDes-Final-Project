# The functionality in this file would be an excellent place to use unit tests!

from hands import *

# This function is very long. Consider breaking it into smaller functions.


def read_hand(hand):
    """reads information from text file for a single hand"""
    all_lines = hand.splitlines()  # list of each line in hand
    seat_count = 0  # make sure hand is only two players!
    round_type = ""
    cards_on_table = []
    round_types = []
    actions = []
    pocket_status1 = []
    pocket_status2 = []
    pot = 0
    for l in all_lines:
        # For an easier way to do this, explore the regular expression library (re).
        # This lets you write patterns that match a string and collect its pieces.
        # For example, something like (untested):
        #  re.match(r'^Seat (\d) - (.+)/(.) \($(\d+\.\d+) in chips\)', l)
        # would match l = 'Seat 3 - 4DyPguwK74ucujjoZHj4/A ($130.04 in chips)'
        # and return a match object m such that
        # m.groups() == ('3', '4DyPguwK74ucujjoZHj4', 'A', '130.4')
        if "Stage" in l:
            stage_num = l[l.find("#") + 1: l.find(":")]
            game_type = l[l.find(":") + 2: l.find("-")]
            date = l[l.find("-") + 2:]
        elif "Table" in l:
            table = l[l.find(":") + 1: l.find("(Real Money)")]
            dealer_seatnum = l[l.find("#") + 1: l.find(" is")]
        elif "in chips" in l:
            if seat_count == 0:
                player1_seatnum = l[l.find(" ") + 1: l.find("-") - 1]
                player1_id = l[l.find("-") + 2: l.find("(") - 1]
                player1_chips = l[l.find("$"): l.find("in") - 1]
                #print("Defined Player 1 ID: ", player1_id)
            elif seat_count == 1:
                player2_seatnum = l[l.find(" ") + 1: l.find("-") - 1]
                player2_id = l[l.find("-") + 2: l.find("(") - 1]
                player2_chips = l[l.find("$"): l.find("in") - 1]
                #print("Defined Player 2 ID: ", player2_id)
            else:
                #print("Hand has more than two players")
                return
            seat_count += 1
        elif "Posts" in l:
            if player1_id in l:
                player1_blind_type = l[l.find(
                    "Posts") + len("Posts"): l.find("blind")]
                player1_blind_amo = l[l.find("blind") + len("blind"):]
                pot += int(player1_blind_amo[2:])
            elif player2_id in l:
                player2_blind_type = l[l.find(
                    "Posts") + len("Posts"): l.find("blind")]
                player2_blind_amo = l[l.find("blind") + len("blind"):]
                pot += int(player2_blind_amo[2:])
        elif "** POCKET CARDS **" in l:
            round_type = "pocket"
            round_types.append(round_type)
        elif "** FLOP **" in l:
            round_type = "flop"
            round_types.append(round_type)
            cards = l[l.find("[") + 1: l.find("]")]
            cards_on_table += cards.split(" ")
        elif "** TURN **" in l:
            round_type = "turn"
            round_types.append(round_type)
            # only one card is ever added at a time after flop
            card = l[l.rfind("[") + 1: l.rfind("]")]
            cards_on_table.append(card)
        elif "** RIVER **" in l:
            round_type = "river"
            round_types.append(round_type)
            card = l[l.rfind("[") + 1: l.rfind("]")]
            cards_on_table.append(card)
        elif "** SHOW DOWN **" in l:
            round_type = "show down"
            # round_types.append(round_type)
        elif "** SUMMARY **" in l:
            round_type = "summary"
            # round_types.append(round_type)
            # print("--------")
            # print("Summary")
            # print("--------")
        # parse through actions in each round (undefined length)
        elif not round_type == "summary" and not round_type == "":
            #round.round_type = round_type
            if player1_id in l:
                if "Folds" in l:
                    play1_act = "fold"
                    # you don't need pass
                elif "Raises" in l:
                    play1_act = "raise "
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                    raise_amo = int(new_amo[1:]) - int(old_amo[1:])
                    pot += raise_amo[1:]
                    play1_act = play1_act + str(raise_amo)
                elif "Calls" in l:
                    play1_act = "call "
                    call_amo = l[l.rfind(" "):]
                    pot += call_amo[1:]
                    play1_act = play1_act + call_amo
                elif "Bets" in l:
                    play1_act = "bet "
                    bet_amo = l[l.rfind(" "):]
                    pot += bet_amo[1:]
                    play1_act = play1_act + bet_amo
                elif "Checks" in l:
                    play1_act = "check"
                # You don't need "else: pass", just document it: Else: Does not show, returns, etc.
            elif player2_id in l:
                # This (mostly – see below) duplicates the player1_id case.
                # This code should be a function that can be applied to
                # player1 and player2, or else code that loops over player1 and player2.
                #
                # Here's the mostly: for player1_id, this first test is "Folds" (note the case).
                # I'm guessing this is an error. This is an example of where the
                # code duplication is problematic.
                if "folds" in l:
                    play2_act = "fold"
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Raises" in l:
                    play2_act = "raise "
                    old_amo = l[l.find("$"): l.find(" to")]
                    new_amo = l[l.rfind("$"):]
                    raise_amo = int(new_amo[1:]) - int(old_amo[1:])
                    pot += raise_amo[1:]
                    play2_act = play2_act + raise_amo
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Calls" in l:
                    play2_act = "call "
                    call_amo = l[l.rfind(" "):]
                    pot += call_amo[1:]
                    play2_act = play2_act + call_amo
                    this_round = (play1_act, play2_act)
                    actions.append(this_round)
                elif "Bets" in l:
                    play2_act = 'bet '
                    bet_amo = l[l.rfind(" "):]
                    pot += bet_amo[1:]
                    play2_act = play2_act + bet_amo
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

    rounds = []
    # create instances
    if player1_seatnum == dealer_seatnum:
        dealer = player1_id
        player1_dealer = True
        player2_dealer = False
    else:
        dealer = player2_id
        player1_dealer = False
        player2_dealer = True
    # or
    #   dealer = player1_id if player1_seatnum == dealer_seatnum else player2_id
    #   player1_dealer = dealer == player1_id
    #   player2_dealer = dealer == player2_id
    # or: I wonder whether you need all three of these variables.

    Player1 = Player(player1_id, player1_chips, player1_dealer,
                     pocket_status1, player1_blind_amo)
    Player2 = Player(player2_id, player2_chips, player2_dealer,
                     pocket_status2, player2_blind_amo)
    players = [Player1, Player2]

    # or:
    for i, rt in enumerate(round_types):
        rounds.append(Round(rt, players, actions[i]))
    # Or:
    #  for rt, action in zip(round_types, actions):
        rounds.append(Round(rt, players, action))

    return rounds

    # This next line is after the return. It is never executed.
    hand = Hand(rounds, dealer, stage_num, pot, table_cards, summary)
    # return hand


def per_hand(file_name):
    """divides text file into hands"""
    # I removed the following comment; it's evident from the code
    with open(file_name, 'rt') as f:
        hand = ""
        prevline = ""
        all_hands = []
        # ditto
        for line in f:
            if line == "\n" and prevline == "\n" and not len(hand) == 0:
                all_hands.append(hand)
                # print(hand)
                hand = ""
            else:
                hand = hand + line
            prevline = line

        return all_hands

# dead code


if __name__ == "__main__":
    all_hands_text = per_hand('small-text.txt')
    all_hands = read_hand(all_hands_text[1])
    # for h in all_hands:
    # read_hand(h)
    print(all_hands)
