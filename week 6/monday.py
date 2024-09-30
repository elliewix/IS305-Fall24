s = "here is some text"

# classic python loop
for character in s:
    print(character)

# sightly weirder python, but sure

for i in range(len(s)):
    print(s[i])

# mimic a bit with a while loop

i = 0 # iterable starting point
while i < len(s):
    # do the business
    print(s[i])
    # increment
    i += 1

##

import random

searching = True
num_runs = 1 # because we're generating a num before we loop
# generate random ints until we see 4, and stop
choice = random.randint(1, 5) # stop is inclusive

print("beginning search")
while searching:
    if choice == 4:
        searching = False # flipping sentinel bc we found it
    else:
        # print(choice, searching)
        choice = random.randint(1,5) # choose a new one
        num_runs += 1 # update the counter

# print("found 4 in", num_runs)

## okay let's make this a proper simulation

import random

all_runs = []
runs = 10000

for i in range(runs):
    # full sim start
    searching = True
    num_runs = 1 # because we're generating a num before we loop
    # generate random ints until we see 4, and stop
    choice = random.randint(1, 5) # stop is inclusive

    # print("beginning search")
    while searching:
        if choice == 4:
            searching = False # flipping sentinel bc we found it
        else:
            # print(choice, searching)
            choice = random.randint(1,5) # choose a new one
            num_runs += 1 # update the counter
    print("found 4 in", num_runs)
    # collect the run numbers up
    all_runs.append(num_runs)
    # sim end

print(all_runs)
print(sum(all_runs)/ runs)