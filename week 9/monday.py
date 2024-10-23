import random

start = "ABBACAA"

# rule of replace any instance of C with ABA

# new = ""
# for letter in start:
#     if letter == "C":
#         new += "ABA"
#     else:
#         new += letter

# print(new)

# now also replace B with D

new = ""
for letter in start:
    if letter == "C":
        new += "ABA"
    elif letter == "B":
        new += "D"
    else:
        new += letter

print(new)


options = ["A", "B", "C"]
probs =   [.35, .35,  .3]

# rule is, we're done when there's no more C's
def replace(line):
    new_line = ""
    for letter in line:

        if letter == "C":
            pick = random.choices(options, weights = probs, k = 3)
            pick_str = "".join(pick)
            # print(pick)
            new_line += pick_str
        else:
            new_line += letter
        # print(new_line)
    if "C" in new_line:
        replace(new_line)
        # print(new_line)
    else:
        print(new_line)
        return None

    return new_line

print(replace("ABBAAACCBBAB"))