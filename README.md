# CS 1440 Assignment 3: Big Data Processing

*   [Instructions](./instructions/README.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit.md)
    *   [Installing the Text Tools](./instructions/Installing_Text_Tools.md)
*   [Project Requirements](./instructions/Requirements.md)
*   [Test Data](./data/README.md)
*   [Performance Benchmark Tool](./demo/README.md)


*Note: this file is a placeholder for your notes.  When seeking help from TAs or tutors, replace this text with a description of your problem and push it to GitLab*


## Get the starter code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3 cs1440-assn3
$ cd cs1440-assn3
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
$ git push -u origin --all
```


## Overview

Your last project was a great success! The customer was very pleased with their new Text Tools and so impressed with the quality of your work that they have decided to contract you to finish the entire project for them.

Your task is to analyze a large body of data and produce a report of the findings.  This program summarizes national employment data collected by the U.S. Bureau of Labor Statistics in 2021.  The report consists of two sections, a summary across all industries and a summary across the software publishing industry.  I worked with the customer far enough to develop the format of the report.  It is your task to analyze a 490MB CSV file to pull out the data needed by the report.


## Shell Tutor Lessons

This assignment includes 2 new [Shell Tutor lessons](./shell-tutor/README.md).  Together they are worth 10 points.  Run `make-certificate.sh` and commit the resulting certificate file in the `shell-tutor` directory.

These lessons should be the **first thing** you do on this assignment.  Complete the tutorial before you begin Phase 0.  As always, if you encounter a problem, run `tutor bug` and email the output to your instructor.


## Expected Program Behavior

Each subfolder of [./data/](data) contains a file named `output.txt`.  Your program's output for that data set should match that file exactly.

Instructions are provided for creating testing data sets using the Text Tools from Assignment #2.  These crafted input files will be the basis of your testing efforts.

Your program should run in a reasonable amount of time.  Use the [Performance Benchmark Tool](./demo/README.md) to learn how fast your program should be.
