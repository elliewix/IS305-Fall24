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

# starting here for Wed content

for fname, content in horse_data.items():
    # pratice printing out the file paths first
    f = pathlib.Path(fname)
    full_path = text_target / f
    # print to check
    # print(full_path) # okay path looks good
    # so we now have the filename and the content
    # which means we are ready to write the files out
    full_path.write_text(content, encoding= 'utf-8')

print(dupes)

## write out a csv
## reusing the headers
## and the content is the dupes list

## write it out using the stand csv pattern

with open('dupe_failures.csv', 'wt', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers) # note the singular row
    csvout.writerows(dupes) # note the plural, give it the 2d list of rows
