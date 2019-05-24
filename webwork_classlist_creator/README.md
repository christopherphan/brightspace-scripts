# WeBWorK Classlist Creator (from D2L Brightspace)

Christopher L. Phan, Ph.D. <cphan@chrisphan.com>

<https://github.com/christopherphan/brightspace-scripts>

## Purpose

The Python script ``webwork_classlist_creator.py`` produces a WeBWorK ``.lst`` file given a ``.csv`` file produced by D2L Brightspace.

This script is written for Python 3.

## Usage

The required input is a CSV file exported from the D2L Brightspace gradebook feature using with the following options:

* Key field: "Both"
* User details: All three checked (last name, first name, and email)


Syntax:
> ``./webwork_classlist_creator.py input-file output-file``

## Important license/warranty notice

Copyright (c) 2019 Christopher L. Phan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
