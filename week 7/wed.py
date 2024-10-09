import random
random.seed(40)

outer = []

inner_temp = []

for i in range(10):
    for j in range(5):
        inner_temp.append(random.choice(" abc"))
    outer.append(inner_temp)
    inner_temp = []

print(outer)

## loop through the 2d list, and fill all empty spaces
# with the character X

# loop through the data

for i, chunk in enumerate(outer):
    for j, content in enumerate(chunk):
        print(content)
        if content == " ":
            outer[i][j] = "X"

print(outer)