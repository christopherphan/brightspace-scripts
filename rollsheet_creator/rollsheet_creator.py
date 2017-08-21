#!/usr/bin/env python3

import csv
import sys
import subprocess

infilename_d2l =  sys.argv[1]
infilename_template =  sys.argv[2]

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
                studentlist_fieldlist[col] = index2
        else:
            if sectionname != "":
                try:
                    student_section = studentlist_fieldlist["Section"]
                except:
                    print("Warning: No section data present!")
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
    out_TeX_file += + "_" + sectionname
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
