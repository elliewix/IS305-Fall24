text = "here's some text and other things"

words = text.split()

# you could use a counter

count = 0
for w in words:
    print(count, w)
    count += 1

# enumerate() can make this cleaner

print(list(enumerate(words)))

# add to our for loop
for w in enumerate(words):
    print(w) # getting the tuple pairs back

# we can do even more
# add enumerate and the variable names in
# but not have to change the core of your loop around

for i, w in enumerate(words):
    print(i, w)
