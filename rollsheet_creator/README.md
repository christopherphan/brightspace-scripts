# Brightspace rollsheet creator

Christopher L. Phan, Ph.D. <cphan@chrisphan.com>

<https://github.com/christopherphan/brightspace-scripts/rollsheet_creator>

## Purpose

The Python script ``rollsheet_creator.py`` produces roll sheet (PDF form), given a CSV file created by the WeBWorK grade export feature in D2L Brightspace.

This script is written for Python 3, and requires a working LaTeX installation.

## Usage

For this script to work, you need 2 files.

First is a D2L Brightspace CSV grade export produced with the following
options:

* Key field: "Both"
* User details: All three checked (last name, first name, and email)
* Optionally: A "Section" field, checked to be exported

Second is a LaTeX template file. This file should have the following:

* A ``\rollsheetbox`` macro which takes one argument, the student's name.
* A line consisting only of the comment>

   > ``%%ROLL NAMES HERE``

* **Optional:** A line consisting only of the comment:

   > ``%%SECTION REPLACE``

This file will create a new LaTeX file, in which ``%%ROLL NAMES HERE`` is replaced with a set of lines of the form ``\rollsheetbox{[student name]}``. If you don't specify a section, then every student in the CSV file will get a ``\rollsheetbox``; otherwise, only students with the "Section" field matching the section argument on the command line will get a ``\rollsheetbox``. The students will be listed in alphabetical order, by surname and then by given name.

If a section is specified at the command line, then the ``%SECTION REPLACE`` line will be replaced with the section.

After the LaTeX file is produced, ``pdflatex`` is run on the file to produce a PDF version of the rollsheet.

An example LaTeX template is given.

Syntax:
>  ``./rollsheet_creator.py [d2l input file] [LaTeX template file] [section]``

The [section] argument is optional.

## Important license/warranty notice

Copyright (c) 2017 Christopher L. Phan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
