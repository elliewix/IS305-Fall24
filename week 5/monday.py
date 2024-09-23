import csv

with open('query.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# print(headers)
# print(len(data))
# print(data[:10])

# now we can loop over the data
# drilling down and collecting data
for r in data:
    # print(r) # looks good
    horse_id = r[0] # index to grab the 1st item
    # print(horse_id) # print as you go to check your work
    url_parts = horse_id.split('/')
    name = url_parts[-1] + ".txt"
    # print(name)
    # stop and collect the data

# we're making a "fake" new section here to see
# how thing built up

horse_data = {}
dupes = []

for r in data:
    horse_id = r[0] # index to grab the 1st item
    url_parts = horse_id.split('/')
    name = url_parts[-1] + ".txt" # my proposed unique value
    if name in horse_data: # check membership
        print("this is a dupe")
        dupes.append(r)
    else:
        # horse_data[name] = "placeholder" # just this for a bit
        horse_data[name] = "\n".join(r)

# print(horse_data)

# loop over the dict of data

# general syntax for dict loops
# for key, value in d.items():

# really put this up top, but for visibility...
import pathlib

text_target = pathlib.Path('content') # this will be our text file folder
text_target.mkdir(exist_ok=True)

print(text_target.exists())

# for fname, content in horse_data.items():



