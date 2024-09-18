# what you need to know before you start writing a custom function

# 1. What's the name of function? Either find it or make it
# 2. What are the inputs? parameters/arguments, etc. and their names?
# 3. What's the point? What's the scope? What is it doing?
# 4. What should it return?

# write a function takes a student's name and grade (numerical),
# then returns back a statement about it
# output: This Student got: 85%.

# 1. create? grade report? create_grade_report
# 2. name, grade. name should be a string, grade should be float?
# 3. format the text per the output
# 4. return the formatted output as a string

def create_grade_report(name, grade):
    # do stuff here
    # example: This Student got: 85%, put a reminder here
    # report = name + " got :" # not done but we can test
    # report = name + " got :" + grade # added but with an error
    # report = name + " got :" + str(grade) # recast grade to string, close but not there
    report = name + " got: " + str(grade) + "%"

    # what to return? the report statement
    # final return statement below, should be the only piece of code
    return report

print(create_grade_report("This Student", 85))

# talking about iteration

names = ["This Student", "That Student", "A Student"]
grades = [78, 95, 86.5]

# well, nesting won't work because that'll give me 9 results

# likewise doing
# for ....
# for....
# won't do it, we need them connected

# but both share index positions

# a classing "range loop, yes you can use i for this one

# this is the mututal index position
for i in range(len(names)): # don't just say 3, use len()
    student_name = names[i] # index on names to the one name
    student_grade = grades[i] # same thing
    print(student_name, student_grade) # not worrying about function yet, just seeing stuff
