import random
import string
from collections import Counter

# say we have 26 letters to choose from
letters = string.ascii_uppercase

# and we choose 50 of them at random, allowing replacement
# with equal chances

random.seed(1)
picks = random.choices(letters, k = 50)
print(picks)
# ideas: for loop, .count() methdod, counter, dict of counters, etc.
counted_picks = Counter(picks)
counted_dict = dict(counted_picks)
# print(counted_picks)
print(counted_dict)

# # DON'T DO THIS
# keys = counted_dict.keys()
# values = counted_dict.values()
#
# print(keys, values)

# a fair first pass

# get's the job done, but has some issues
# for l in letters:
#     # can't just look it up because it may not be there
#     # print(counted_dict[l])
#     print(l, picks.count(l))

headers = list(string.ascii_uppercase)
print(headers)
# remember that the counts are in counted_dict
# how do we connect these counts with headers and then to
# our empty lists??

empty_list = [0] * len(headers)
print(empty_list)
for l, count in counted_dict.items():
    index = headers.index(l)
    empty_list[index] = count
    # print(l, count)
print(empty_list)

