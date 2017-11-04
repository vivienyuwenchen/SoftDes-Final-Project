def read_hand(hand):
    """reads information from text file for a single hand"""


def per_hand(file_name):
    """divides text file into hands"""
    with open (file_name, 'rt') as f:  # Open input file for reading of text data.
        hand = ""
        prevline = ""
        all_hands = []
        for line in f: # Store each line in a string variable "line"
            if "Stage" in line:
                stage_num = line # fake news
            elif line == "\n" and prevline == "\n":
                all_hands.append(hand)
                print(hand)
                hand = ""
            else:
                hand = hand + line + "\n"
            prevline = line
        print(len(all_hands))

if __name__ == "__main__":
    per_hand('small-text.txt')
