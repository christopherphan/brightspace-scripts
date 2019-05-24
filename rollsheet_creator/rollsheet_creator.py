#!/usr/bin/env python3

# rollsheet_creator.py
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
rollsheet_creator.py

Copyright (c) 2019 Christopher L. Phan

See README.md or source code for important license and disclaimer of warranty
notice.

Creates a rollsheet from a CSV file exported from D2L Brightspace.

For this script to work, you need 2 files.

First is a D2L Brightspace CSV grade export produced with the following
options:

Key field: "Both"
User details: All three checked (last name, first name, and email)
Optionally: A "Section" field, checked to be exported

Second is a LaTeX template file. See README.md for details.

syntax: ./rollsheet_creator.py d2l-input-file LaTeX-template-file [section]

The [section] argument is optional.
"""

import csv
import sys
import subprocess

infilename_d2l =  sys.argv[1]
infilename_template =  sys.argv[2]

if len(sys.argv) < 3 or len(sys.argv) > 5:
    print(help_string)
    sys.exit()

if len(sys.argv) == 4:
    sectionname = sys.argv[3]
else:
    sectionname = ""

# Step 1: Read the list of students from the D2L download

studentlist = []
studentlist_fieldlist = dict()

with open(infilename_d2l, 'rt') as infile:
    studentreader = csv.reader(infile, delimiter=',')
    for (index, row) in enumerate(studentreader):
        if index == 0:
            for (index2, col) in enumerate(row):
                studentlist_fieldlist[col.split("Text")[0].strip()] = index2
        else:
            if sectionname != "":
                student_section = row[studentlist_fieldlist["Section"]]
            else:
                student_section = ""
            if (sectionname == "" or sectionname == student_section):
                studentlist.append((
                    row[studentlist_fieldlist["Last Name"]],
                    row[studentlist_fieldlist["First Name"]]
                    ))

# Step 2: Sort the list alphabetically
studentlist.sort()

# Step 3: Output a LaTeX class list

out_TeX_file = infilename_d2l + "_rollsheet"
if sectionname != "":
    out_TeX_file += "_" + sectionname
out_TeX_file += ".tex"

with open(infilename_template, 'rt') as template_file:
    with open(out_TeX_file, 'wt') as outputfile:
        for line in template_file:
            if line.strip() == "%%ROLL NAMES HERE":
                for student in studentlist:
                    outputfile.write("\\rollsheetbox{" +
                        student[0] + ", " + student[1] + "}\n")
            elif line.strip() == "%%SECTION REPLACE" and sectionname != "":
                outputfile.write(sectionname + "%\n")
            else:
                outputfile.write(line)

# Step 4: Compile!

subprocess.call(["pdflatex", out_TeX_file])
