""" 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


"""


import csv


# create a file object to open the file in read mode

infile = open("students.csv", "r")

# create a csv object from the file object

students_file = csv.reader(infile, delimiter=",")

# skip the header row

next(students_file)

# create an outfile object for the pocessed record

outfile = open("processedstudents.csv", "w")

# create a new dictionary named 'student_dict'

student_dict = {}

# use a loop to iterate through each row of the file

# check if the GPA is below 3.0. If so, write the record to the outfile

for gpa in student_dict.gpa:
    if gpa in student_dict < 3.00:
        outfile.write()
    else:
        next(gpa)
print()


# append the record to the dictionary with the student id as the Key
# and the value as the GPA

student_dict = {"stud_id": "gpa"}


# print the entire dictionary

print(student_dict)

# Print the student id

stud_id = student_dict["stud_id"]["6"]
print(stud_id)

# print out the corresponding GPA from the dictionary

gpa = student_dict["gpa"]["6"]
print(gpa)

# close the outfile

outfile.close()
