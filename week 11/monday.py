import sqlite3

conn = sqlite3.connect('pettigrew.db')
c = conn.cursor()

results = c.execute("SELECT * FROM letters;")
print(results) # get cursor object
print(results.description)
for h in results.description:
    print(h[0])

# the cursor will be moving as you go
# print(results.fetchone()) # single row
# print(results.fetchmany(5))
# print(results.fetchall()) # remainder of the data

# skipping the above
# lets me use the results object without
# the cursor being moved

all_data = results.fetchall()

print(all_data)

import csv

# construct the headers

headers = [r[0] for r in results.description]
print(headers)
# we already have all the data within all_data

with open('letter_data.csv', 'wt', encoding='utf-8') as infile:
    csvout = csv.writer(infile)
    csvout.writerow(headers)
    csvout.writerows(all_data)


# from the other way around

with open('letter_data.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(data)

# we're going to create a new database file

conn = sqlite3.connect('new_letters.db') # give it a file name that's new
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS letters (box string, folder string, desc string, date string)") # create the table

c.executemany("INSERT INTO letters VALUES(?, ?, ?, ?)", data)

new_results = c.execute("select * from letters;")

print(new_results.description)
all_new_results = new_results.fetchall()

# save results
conn.commit()
conn.close()