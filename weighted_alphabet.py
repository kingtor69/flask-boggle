# Tor Kingdon made this for a Boggle probject based on the idea that Boggle dice have more common letters appreading more often than 1 in every 26 squares on a Boggle board
# the information about common languages come from the Oxford Dictionary (11th edition revised, 2004) as presented on https://www.lexico.com/explore/which-letters-are-used-most
# I've also used some of the common letter combinations some editions of Boggle used (as described on https://en.wikipedia.org/wiki/Boggle)

from random import choice, randint

weighted_lowercase_alphabet = ""
for j in range(10):
    weighted_lowercase_alphabet += "j"
for z in range(14):
    weighted_lowercase_alphabet += "z"
for x in range(15):
    weighted_lowercase_alphabet += "x"
# according to Oxford, this should be the same as J, but given the substitution to Qu (below) I thought it deserved to show up more often
for q in range(30):
    weighted_lowercase_alphabet += "q"
for v in range(51):
    weighted_lowercase_alphabet += "v"
for k in range(56):
    weighted_lowercase_alphabet += "k"
for w in range(66):
    weighted_lowercase_alphabet += "w"
for y in range(90):
    weighted_lowercase_alphabet += "y"
for f in range(92):
    weighted_lowercase_alphabet += "f"
for b in range(106):
    weighted_lowercase_alphabet += "b"
for g in range(126):
    weighted_lowercase_alphabet += "g"
for h in range(153):
    weighted_lowercase_alphabet += "h"
for m in range(154):
    weighted_lowercase_alphabet += "m"
for p in range(161):
    weighted_lowercase_alphabet += "p"
for d in range(173):
    weighted_lowercase_alphabet += "d"
for u in range(185):
    weighted_lowercase_alphabet += "u"
for c in range(231):
    weighted_lowercase_alphabet += "c"
for l in range(280):
    weighted_lowercase_alphabet += "l"
for s in range(292):
    weighted_lowercase_alphabet += "s"
for n in range(339):
    weighted_lowercase_alphabet += "n"
for t in range(354):
    weighted_lowercase_alphabet += "t"
for o in range(365):
    weighted_lowercase_alphabet += "o"
for i in range(385):
    weighted_lowercase_alphabet += "i"
for r in range(386):
    weighted_lowercase_alphabet += "r"
for a in range(433):
    weighted_lowercase_alphabet += "a"
for e in range(569):
    weighted_lowercase_alphabet += "e"

weighted_uppercase_alphabet = weighted_lowercase_alphabet.upper()

def random_letter_plus_combos():
    ltr = choice(weighted_uppercase_alphabet)
    roll = ltr
    # this wasn't working
    # it's going to have to wait for future development
    # if ltr == "Q":
    #     roll = "Qu"
    # elif ltr =="T":
    #     if randint(1, 3) == 1:
    #         roll = "Th"
    # elif ltr == "I":
    #     if randint(1, 5) == 1:
    #         roll = "In"
    return roll

