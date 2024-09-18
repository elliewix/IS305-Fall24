names = ["This Student", "That Student", "A Student"]
grades = [78, 95, 86.5]
#
# # mutual index
# for i in range(len(names)):
#     print(i, names[i], grades[i])
#

# zip method

print(zip(names, grades)) # you'll see a "generator" object

# but if you want to see the stuff inside, recast to a list
pairs = list(zip(names, grades))
print(pairs)

# for something in pairs: # cool but we can do better
#     print(something)

# for name, grade in pairs:
#     # print(name, grade)
#     print(name + "'s grade was " + str(grade))
# the more natural way to do it, but converting into a list
# and looping over that is also fine
for name, grade in zip(names, grades):
    print(name, grade)


# but what is zip really doing??

pairs = zip( range(0, 5), range(10, 20) )
pairs = list(pairs)

print(pairs)

# assert statements
# assert keyword, then a boolean arugment/check

assert len(grades) == len(names) # if True, nothing happens

grades.append(77) # add something so len is now 4
# commented out to suppress the error
# assert len(grades) == len(names), "lengths don't match"

# logic statements in python

text = ["some", "text", "stuff", "x", "", " ", "2"]

for t in text:
    print(t, len(t))
    # no if ladder!
    # if len(t) == 0:
    #     print("empty string")
    # if len(t) == 1:
    #     print("one character")
    # if len(t) > 1:
    #     print("more than one character")

    # better, don't leave if lonely unless you really need to

    if len(t) == 0:
        print('empty string')
    else:
        print("not an empty string")

    # best

    if len(t) == 0:
        print("empty string")
    elif len(t) == 1:
        print("one character")
    else:
        print("more than one")