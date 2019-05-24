#! /usr/bin/env python3

# webwork_classlist_creator.py
#
# Christopher L. Phan, Ph.D.
# cphan@chrisphan.com
# Last updated: 2019-05-23
#
#################################

# Copyright (c) 2019 Christopher L. Phan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import csv

help_string = """
webwork_classlist_creator.py

Copyright (c) 2019 Christopher L. Phan

See README.md or source code for important license and disclaimer of warranty
notice.

Produces a WeBWorK .lst file given a .csv file produced by D2L Brightspace

syntax: ./webwork_classlist_creator.py input-file output-file

The CSV file should be produced by the Export Grades feature on D2L Brightspace
with the following options:

Key field: "Both"
User details: All three checked (last name, first name, and email)
"""

if len(sys.argv) != 3:
    print(help_string)
    sys.exit()

infilename =  sys.argv[1]
outfilename = sys.argv[2]

students = []

with open(infilename, 'rt') as infile:
    studentreader = csv.reader(infile, delimiter=',')
    for row in studentreader:
        students.append(row)

with open(outfilename, 'w') as outfile:
    for (index, student) in enumerate(students):
        if index == 0:
            columndict = dict()
            for (index2, col) in enumerate(student):
                columndict[col] = index2
        else:
            outstring = '{studentid},{lastname},{firstname},C,,,,{email},{username},,\n'.format(
                         studentid=student[columndict['OrgDefinedId']][1:],
                         lastname=student[columndict['Last Name']],
                         firstname=student[columndict['First Name']],
                         email=student[columndict['Email']],
                         username=student[columndict['Username']][1:])
            outfile.write(outstring)
