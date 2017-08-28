# WeBWorK Grades to Brightspace

Christopher L. Phan, Ph.D. <cphan@chrisphan.com>

<https://github.com/christopherphan/brightspace-scripts>

## Purpose

The Python script ``webwork_grades_to_brightspace.py`` converts a WeBWorK grade export file to a format that can be imported by D2L Brightspace.

This script is written for Python 3.

## Usage

For this script to work, you need 2 files:

First is a CSV file exported from the D2L Brightspace gradebook feature using with the following
options:

* Key field: "Both"
* User details: All three checked (last name, first name, and email)

Second is the WeBWorK grade export. NOTE: We assume the student's userid on
WeBWorK is the same as their userid on D2L Brightspace (in the case of
Minnesota State students, that would be their StarID).

Syntax:
> ``./webwork_grades_to_brightspace.py [d2l input file] [WeBWorK input file] [D2L output file]``

## Important license/warranty notice

Copyright (c) 2017 Christopher L. Phan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
