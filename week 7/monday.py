with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    # read it all in as one str variable
    data = infile.read()

lines = data.splitlines()

# this file is a bunch of x,y,z coords but all just flat
# in one "column" of data
# reconstruct those groups of xyz points into a 2d list

# we aren't sure yet how to do it, but we can
# start with setting up what we're sure about

corrected_points = [] # will get all the new trios
one_set_of_points = [] # will hold each xyz at a time
# count the number of lines we see
# count = 1
# for point in lines: # prob at least need to loop over it
#     if count > 3: # collect/reset
#         corrected_points.append(one_set_of_points) # collect the "finished" set
#         # then reset
#         one_set_of_points = []
#         count = 1
#     else: # still gathering
#         one_set_of_points.append(point)
#         count += 1
#
#     print(one_set_of_points)

# well I could get that to wokr but it's weird


corrected_points = [] # will get all the new trios
one_set_of_points = [] # will hold each xyz at a time

# # clusting process
# for p in lines:
#     one_set_of_points.append(p)
#     print(one_set_of_points)
#     if len(one_set_of_points) == 3:
#         #collect
#         corrected_points.append(one_set_of_points)
#         # reset
#         one_set_of_points = []
#
# # let's check the work
# import time
# print(corrected_points) # can be hard to see at once
# for groups in corrected_points:
#     print(groups)
#     # time.sleep(5)

sen = "this is a cat, cats are cool"
words = sen.split()
bigrams = []
temp = []
for i, current in enumerate(words):
    # print(i, current)
    temp.append(current)
    # add protection zone
    next_i = i + 1
    if next_i == len(words):
        print("done")
    else:
        next_word = words[i + 1]
        temp.append(next_word)
        print(current, next_word, temp)
        if len(temp) == 2:
            bigrams.append(temp) # collect
            temp = [] #reset`   

print(bigrams)