import random

# replacement rule systems

# generate a fake landscape
# take a series of dots some length, but div by 3

length = 11
actual_length = length * 3
base = "." * actual_length

# divide that by 3, remove the middle 3rd

def remove_third(base):
    l = int(len(base) / 3) # this should be even given how I made it
    print(l)
    left = (0, l)
    right = (l * 2, l * 3)
    new_line = [' '] * len(base)
    for i in range(left[0], left[1]):
        new_line[i] = '.'
    for i in range(right[0], right[1]):
        new_line[i] = '.'
    print("".join(new_line))

remove_third(base)

def make_cantor(length, section = "start"):
    section_length = int(length / 3)
    if section == "start":
        print(section_length * 3 * ".")
    elif section == "l":
        print("." * length, end = "")
    elif section == "c":
        print(" " * length, end = "")
    elif section == "r":
        print("." * length)
    if length < 3:
        return 0
    make_cantor(section_length, "l")
    make_cantor(section_length, "c")
    make_cantor(section_length, "r")



make_cantor(3 ** 3)