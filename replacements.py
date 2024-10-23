import random

random.seed(89)

options = ["A", "B", "C"]
probs =   [.35,  .35,  .3]

# iteratively replace C with these choices until C is gone
# replace A with a random value and a B
def make_string(line):
    for i, l in enumerate(line):
        if l == "C":
            line[i] = random.choices(options, weights = probs, k = 1)[0]
        elif l == "A":
            add_these_two = random.choices(options, weights = probs, k = 2)
            line[i] = add_these_two[0]
            line.insert(i + 1, "B")
    print(line)
    if "C" in line:
        make_string(line)
    else:
        print("done!")
        return None


start = random.choices(options, weights = probs, k = 5)
print(start)
make_string(start)