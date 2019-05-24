#! /usr/bin/env python3

# webassign_grades_to_brightspace.py
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

help_string = """
webassign_grades_to_brightspace.py

Copyright (c) 2019 Christopher L. Phan

See README.md or source code for important license and disclaimer of warranty
notice.

Converts a WebAssign grade export file to a format that can be imported under D2L Brightspace.

For this script to work, you need 2 files:

First is a CSV file exported from the D2L Brightspace gradebook feature using with the following
options:

* Key field: "Both"
* User details: All three checked (last name, first name, and email)
* A "WebAssignUsername" field with their WebAssign Username

Second is the WebAssign grade export, exported in "tsv" format.

syntax: ./webassign_grades_to_brightspace.py d2l-input-file WeBWorK-input-file D2L-output-file
"""

import csv
import sys

if len(sys.argv) != 4:
    print(help_string)
    sys.exit()

infilename_d2l =  sys.argv[1]
infilename_wa =  sys.argv[2]
outfilename = sys.argv[3]


# Step 1: Read the list of students from the D2L download

studentlist = dict()

with open(infilename_d2l, 'rt') as infile:
    studentreader = csv.reader(infile, delimiter=',')
    for (index, row) in enumerate(studentreader):
        if index == 0:
            wa_un_idx = row.index("WebAssignUsername Text Grade <Text>")
        else:
            studentlist[row[wa_un_idx].strip()] = (row[0].strip(), row[1].strip())

# Step 2: Scrape out the scores

setnames = []

with open(infilename_wa, 'rt') as infile:
    wareader = csv.reader(infile, delimiter='\t')
    studentpart = False
    for row in wareader:
        if studentpart:
            curstudent = row[1].strip()
        if (studentpart and curstudent in studentlist):
            output.append([studentlist[curstudent][0], studentlist[curstudent][1]])
            for column in setnames:
                curscore = row[column[1]].strip()
                if (curscore == "NS" or curscore == "ND" or curscore == ""):
                    curscore = "0"
                output[-1].append(curscore)
            output[-1].append("#")
        if (row != [] and not studentpart):
            if (row[0].strip() == "Assignment Name"):
                # Read off the set names and store in "setnames"
                for (idx2, column) in enumerate(row):
                    if (column.strip() !="" and column.strip() != "Total" and
                        column.strip() != "Assignment Name"):
                        assign_name = column.strip()
                        assign_name = assign_name.replace(",", " ")
                        setnames.append([assign_name, idx2])
            elif (row[0].strip() == "Totals"):
                # Read off the value names and put in the set names
                for column in setnames:
                    column.append(row[column[1]].strip())
            elif (row[0].strip() == "Fullname"):
                # We are ready to read the scores, set up the output
                output = [['OrgDefinedId', 'Username']]
                for column in setnames:
                    output[0].append(column[0] + " Points Grade <Numeric MaxPoints:" + column[2] + ">")
                output[0].append("End-of-Line Indicator")
                studentpart = True

# Step 3: Output

with open(outfilename, 'wt') as outfile:
    for row in output:
        outline = ""
        for column in row:
            outline += column
            if (column != "#" and column != "End-of-Line Indicator"):
                outline +=","
        outfile.write(outline + "\n")
