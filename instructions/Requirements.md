# CS 1440 Assignment 3: Big Data Processing - Project Requirements

*   Write a Python program that summarizes the Bureau of Labor Statistics' employment data for the year 2021.  
*   The data is read from a pair of plain text Comma Separated File (CSV) files.
*   Apply **lessons** learned from the previous assignment to this project. 
    *   Do not copy code over from the last assignment; draw inspiration from it!


## Shell Tutor Lessons

*   This assignment includes two new Shell Tutor lessons in [shell-tutor](./shell-tutor/).
*   Together they are worth 10 points.
    *   Run `make-certificate.sh` and commit the resulting certificate file in the `shell-tutor/` directory.
*   Complete the lessons before you begin the project.
    *   They teach new Git techniques that are required on this assignment.
*   As always, if you run into a problem with the tutorial, run `tutor bug` and email the output to your instructor.


## Command Line Interface

*   Unlike the previous assignment, this program takes exactly one argument, the name of a *directory*, not a *file*.
*   This program is an exception to our general rule about hard-coding file names into programs.
    *   For this assignment you *must* hard-code the names of the input files `area-titles.csv` and `2021.annual.singlefile.csv` into your program.
    *   Do not hard-code the directories containing these files.
    *   Do not code any assumptions about the program's current directory.  The program must work when run from *any* directory.
*   Do not read too much into the naming convention used by the data directories.
    *   The name of the directory containing this file **does not matter** to your program
    *   Your program must be able to work with *any* directory name that can be supplied on the command line, even directories not included with the starter code.
    *   For example, if `2021.annual.singlefile.csv` contains data only about Idaho but is in a directory named `"South_Dakota"`, your program will still print a report about Idaho.

To compute statistics for the entire economy of Washington D.C., from the repository's top directory run:

```
$ python src/bigData.py data/DC_complete
```

To generate the report against the national database, use this command:

```
$ python src/bigData.py data/USA_full
```

When the argument is omitted a message is printed and the program exits:

```
$ python src/bigData.py
Usage: src/bigData.py DATA_DIRECTORY
```

When the specified directory is non-existent or inaccessible, let Python's `open()` function fail:

```
$ python src/bigData.py data/DERP
Traceback (most recent call last):
  File "src/bigData.py", line 220, in <module>
    fips = get_fips_areas(sys.argv[1])
  File "src/bigData.py", line 9, in get_fips_areas
    with open(f'{datadir}/area-titles.csv') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/DERP/area-titles.csv'
```


## Program Speed

*   This program should finish in a *reasonable* amount of time
    *   You won't get a better grade if your program is *extra fast*
    *   You will lose points if your program is *too slow*
*   Because everybody's computer is different, one time limit is not fair
    *   Instead, use the [Performance Benchmark Tool](../demo/README.md) to see what a *reasonable* amount of time means for your computer


## Report Format

This repository contains sample input directories under `data/`, each of which contains three files:

*   `README.md`
    -   Instructions for trimming the full data set down using command line text tools
*   `area-titles.csv`
    -   The database of FIPS area codes
*   `output.txt`
    -   The correct output for this data set

This program's output must *exactly match* the examples down to the smallest detail.

*   The only output that should appear on STDOUT is produced by `print_report(rpt)`
    *   Your final submission *must not* print any other data to `sys.stdout`.
    *   Delete all of the `print()`s that output **TODO** messages
    *   You may keep calls to `print()` that write to STDERR
*   Check that your program finds the correct answers by redirecting its STDOUT to a file, and comparing that to the examples:
    *   ```bash
        $ python src/big_data.py data/UT_all_industries > ut.txt
        $ diff -u ut.txt data/UT_all_industries/output.txt
        ```
    *   The `diff` text tool shows differences between two files
        *   Its output is most readable when run as `diff -u File0 File0`
*   This is how we will grade your submission!


### Filling in the report

*   The starter code provides a module called `report.py`
    *   **Do not modify** `report.py`.  Consider it read-only.
    *   You may create new modules if desired.
*   Study the starter code to learn how to use the report dictionary.
    *   Avoid creating extra variables by using `rpt` for storage.
    *   Some fields within `rpt` hold integers, while others hold lists.


## Can I use Python's `csv` module?

No.  

*   For this assignment, `csv` provides no essential capabilities over the `str` class.
*   More importantly, the point of this assignment is to teach you how to process data *generally*.
    *   The `csv` module won't teach you how to solve problems when your data comes in a different format than CSV.
*   Put another way, CSV is a subset of plain text data.
    *   If you know how to deal with plain text you can deal with CSV, but the converse isn't necessarily true.
    *   You limit yourself if you can only solve problems when a module exists.

![](./consoomer.jpg "One of the programmers who will lose his job to Chat GPT this year")

Don't merely be a consumer; you can be the programmer who *makes* modules.  _(And don't even ask about using `numpy`.  This assignment really isn't that complicated.)_


## Processing `area-titles.csv`

While the file name `area-titles.csv` is hard-coded into your program, the name of the directory containing it is specified by the user.

This CSV file contains two columns of data, `area_fips` and `area_title`.  These columns map a FIPS area code into a familiar place name.


### FIPS Codes

A FIPS code is a 5 character alphanumeric code similar to a ZIP code.  A FIPS area can be a county, an entire state, or a metropolitan area.  There are even FIPS codes which represent the nation as a whole.  The area designated by a FIPS area code is much larger than a ZIP code, and one place may be represented by many overlapping FIPS areas. It is important for the accuracy of the report that overlapping areas excluded so as to not double-count statistics.

The format of FIPS area codes are described in [QCEW Area Codes and Titles](https://data.bls.gov/cew/doc/titles/area/area_guide.htm).  Part of the assignment is to read and thoroughly understand this document.



### How to use `area-titles.csv`

*   Do not modify `area-titles.csv`; just use it as-is
*   Read it one line at a time
    *   Decide whether or not to include this FIPS area in the final report by looking at the FIPS area code
    *   Your program can make this determination *solely* from the `area_fips` field; do not consider the `area_title`
*   Read the `help()` documentation for `str.split` to learn how to split each line of this file into *exactly* two fields regardless of the number of commas it contains.
*   Keep track of FIPS areas that may be included in the report in a **dictionary**
*   The report *must* include data from all 50 states, the District of Columbia, and territories of the United States of America.
    *   This includes:
        *   Puerto Rico
        *   Virgin Islands
        *   "Overseas Locations"
        *   "Multicounty, Not Statewide"
        *   "Out-of-State"
        *   and "Unknown Or Undefined" areas
    *   All of these are *easily* identified by looking only at their FIPS codes
*   The report considers data only from counties and county-equivalent divisions
    *   For example, Louisiana has *parishes*, Alaska has *boroughs* and *census areas*, and Puerto Rico has *municipios*
*   Exclude these areas:
    *   "U.S. combined" and "TOTAL" FIPS areas
    *   All areas labeled "statewide"
    *   MicroSAs
    *   MSAs
    *   CSAs
    *   Federal Bureau of Investigation – undesignated
*   Including these FIPS areas makes your report double- and triple-count areas
    *   *Again, all of these can easily be identified by looking at their FIPS codes*
*   FIPS area codes follow a *simple pattern* which makes it easy to exclude unwanted areas
    *   If your code considers the human-friendly area title, you're doing it wrong
*   While some FIPS area codes look like integers, *always* treat them as strings
*   `area-titles.csv` contains 4,726 lines of text, of which the first is a CSV header line
    *   After discarding unwanted FIPS areas you will be left with 3,463 FIPS areas


## Processing `2021.annual.singlefile.csv`

As with the file `area-titles.csv`, the file name `2021.annual.singlefile.csv` shall be hard-coded into your program.  The name of the directory in which this file is found is supplied by the user.

Each line of this file captures employment statistics such as total wages paid, the number of people employed and the number of establishments in each FIPS area for the year 2021.  The layout of this CSV file is described by [QCEW Field Layouts](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm).  _Hint: We are using the **singlefile**_.

The fields in this file that are significant for our report are:

*   `area_fips`
*   `industry_code`
*   `own_code`
*   `total_annual_wages`
*   `annual_avg_emplvl`
*   `annual_avg_estabs`


### How to use `2021.annual.singlefile.csv`

*   Only one line of this file's text should be stored in memory at a time
    *   Don't slurp the entire file into a variable as one giant string or as an array
        *   To be crystal clear: don't use `.read()` or `.readlines()`
        *   You may make temporary copies of the *current* line, and keep select information from it
        *   Once you've finished with the current line of the file, you don't need to refer back to it again
*   Your program will skip over the vast majority of lines in this file as it seeks the few data points our customer wants
    *   In addition to skipping over lines representing excluded FIPS areas, it will also skip lines that don't belong to the sectors of the economy our customer is interested in
*   Any line of this file with the desired values for `area_fips`, `industry_code`, and `own_code` *must* be included in the report
*   Numeric data must be converted from a string through an appropriate function
    *   `eval()` is **inappropriate**


### Excluded FIPS areas

Some lines contain data for areas that do not belong in the report.   Identify which lines your program should skip over by inspecting the `area_fips` column.  See the section above titled *How to use the information from `area-titles.csv`*.


### All Industries

If a line of the file pertains to a reportable FIPS area and `industry_code` is equal to `"10"` and `own_code` is equal to `"0"`, then its data is added to the "all industries" portion of the report.


### Software Publishing Industry

If a line of the file pertains to a reportable FIPS area and `industry_code` is equal to `"5112"` and `own_code` is equal to `"5"`, then its data is added to the "software publishing industry" portion of the report.

**No other industry codes or ownership codes have a place in the report.**


### Make It Work Before You Make It Fast

*   Don't even think about making your program faster until it consistently gives *correct answers*.
*   The CSV file in `USA_full` is very large, and your program will need time to process it.
    *   `demo/benchmark.py` helps you know how fast your program should be on your computer.
    *   If your program is slower than what the benchmark suggests, you are doing something wrong!

> Programmers waste enormous amounts of time thinking about, or worrying about,
> the speed of noncritical parts of their programs, and these attempts at
> efficiency actually have a strong negative impact when debugging and
> maintenance are considered.  We should forget about small efficiencies, say
> about 97% of the time: premature optimization is the root of all evil.
> Yet we should not pass up our opportunities in that critical 3%.
> 
> – Donald Knuth
> "Structured Programming With Go To Statements"
> Computing Surveys, Vol 6, No 4, December 1974


#### Efficiency Tips

*   Minimize the number of times your program reads each file.  One pass per file is enough.
*   Minimize the number of `for` loops that are nested within other loops.  You can solve this problem with only two separate, un-nested `for` loops.
*   Do not read a file into an array and *then* loop through the array.  Simply loop through the lines of the file, one at a time.
*   Do not use a list or tuple to store the mapping of FIPS area codes to human-readable area titles.  Use a dictionary. 
