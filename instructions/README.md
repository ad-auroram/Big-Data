# CS 1440 Assignment 3: Big Data Processing - Instructions

## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:----------
Average Hours Spent              | 9.8
Standard Deviation Hours         | 4.0
Average Score % (Grade)          | 82.5% (B-)
% students thought this was Easy | 32.4%
... Medium                       | 48.0%
... Hard                         | 12.7%
... Too Hard/Did not complete    | 5.9%


*   [How to Do This Assignment](#how-to-do-this-assignment)
    *   [Phase 0: Requirements Specification](#phase-0-requirements-specification)
    *   [Phase 1: Design](#phase-1-design)
    *   [Phase 2: Implementation](#phase-2-implementation)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging)
    *   [Phase 4: Deployment](#phase-4-deployment)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [What We Look for When Grading](#what-we-look-for-when-grading)
*   [Important Things to Watch Out For](#important-things-to-watch-out-for)


## How to Do This Assignment

*   Beginning with this assignment you will use **Git tags** to mark your progress through the Software Development Process.
*   Before you start on the code, complete the [Shell Tutor lessons](../shell-tutor/README.md) so you know how to do this.
    *   Incorrectly spelled/capitalized tags are ignored.
    *   **If you tag a wrong commit**, or **incorrectly spell a tag** refer to `Using_Git/Intermediate_Git.md` in the lecture notes for instructions.




### Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change any code in this phase**

0.  Read the [Project Requirements](./Requirements.md) to orient yourself with the project.
1.  Read the BLS documents that describe the data: 
    *   [QCEW Area Codes and Titles](https://data.bls.gov/cew/doc/titles/area/area_guide.htm)
    *   [QCEW Field Layouts](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm)
2.  **Do not change the source code in this phase of the project!**
    *   You will edit code in **Phase 2: Implementation**.
    *   In this phase your task is to *draft* the plan that you will follow when you get there.
3.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the assignment is due
4.  Fill out **Phase 0** in Plan.md; explain in your *own words* what the program does, how it does it, and what changes you expect to make.
5.  Track your time in Signature.md.
6.  Tag the last commit in this phase `requirements`
    -   *Grace Points: if this tag is pushed by end of day the Sunday before the due date, you will receive up to 5 points back from other lost points on this assignment*


### Phase 1: Design
*(30% of your effort)*

**Important - do not change any code in this phase**

0.  Design your functions on paper; **don't rewrite the Python code yet**.
    *   In this phase sketch out your *pseudocode*.
    *   Do not paste Python code into Plan.md; when we want to see your code we will read the `.py` files.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your design will work.
1.  You may write *some* runnable Python code to test out your ideas.
    *   This is called *prototyping*, and is a normal part of the design process.
    *   Do not become too attached to your prototype!
    *   Be prepared to delete prototype code after this phase.
    *   It helps to *not* write prototype code in the same files as *real* code.
2.  You should be able to get 100% on the **Starter Code Quiz** by now.
3.  Fill out **Phase 1** in Plan.md.
    *   This will be the longest portion of the document.
4.  Track your time in Signature.md.
5.  Tag the last commit in this phase `designed`
    -   *Grace Points: if this tag is pushed by end of day the Sunday before the due date, you will receive up to 5 points back from other lost points on this assignment*


### Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

0.  Prepare the [data sets](./data/README.md) for testing
    *   The USA Full data set is too large to include in this Git repository
    *   Download [2021.annual.singlefile.zip](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn3/uploads/25c7f05127d7730c0e9d6a14d6b977f1/2021_annual_singlefile.zip) from GitLab and unzip it into `data/USA_full/`
    *   Do not obtain this file from anywhere else; there is a chance they will change it without warning, rendering your output different from the provided examples.
    *   Unzip it into the `data/USA_full/` directory
    *   A `.gitignore` file protects you from committing large CSV files.  Contact your instructor if one is somehow committed!
    *   Follow the instructions in each sub-directory to create smaller data sets for testing
    *   Data sets with `_reversed` names are identical to the corresponding `_complete` data sets save for one difference - they are created with `tac` instead of `cat`.  This reversal of their contents should make no difference to your program.  Use these data sets to ensure this is the case.
1.  Run `python demo/benchmark.py data/USA_full/` and note how long the program ought to run on your computer.
2.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes unexpectedly!
    *   Don't forget to **close all files** your program uses.
3.  Fill out **Phase 2** in Plan.md.
    *   As you work in this phase you may choose to deviate from the design you settled upon in the previous phase.  This is normal!
    *   Briefly explain what changed.
    *   Do not paste long passages of Python code in Plan.md.
    *   Your write-up for this phase may be very short.
4.  Track your time in Signature.md.
5.  Tag the last commit in this phase `implemented`


### Phase 3: Testing and Debugging
*(30% of your effort)*

0.  Run your program against all data sets.
    *   Your submission will be graded with `USA_full` and a **special, crafted data set** that you do have not seen.
    *   To ensure that your program gets full marks, test it thoroughly!
1.  Fill out **Phase 3** in Plan.md.
    *   Describe the tests cases you ran.
    *   Make note of the commands that you ran and what happened in the program.
2.  If you found bugs in this phase, explain what was wrong and how you fixed it.
3.  Track your time in Signature.md.
4.  Tag the last commit in this phase `tested`


### Phase 4: Deployment
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Assignment](./How_To_Submit.md) and make sure that your submission is correct.
1.  Tag the last commit in this phase `deployed`
2.  Push your code to GitLab, then check that all of your files, commits and **tags** appear there.
3.  Clone your project into a *different directory*, and re-run your test cases.
    *   Run `git log` and verify that all tags are present and on the correct commit.


### Phase 5: Maintenance

0.  Review your Plan.md and Signature.md one last time.
1.  Fill out **Phase 5** in Plan.md by answering the questions.
2.  Make one final commit and push your **completed** Software Development Plan and Signature to GitLab.
3.  Make sure that you are happy with your **Starter Code Quiz** score.
4.  Respond to the **Assignment Reflection Survey** on Canvas.



## What We Look for When Grading

**Total points: 100**

*   Shell Tutor Lessons are completed (10 points)
    *   The file `shell-tutor/certificate.txt` is present
*   Quality documentation (35 points)
    *   Plan.md
        *   Each section filled out with a convincing level of detail
        *   No code is pasted from the source files
    *   Signature.md
        *   All development activities are accounted for
        *   Placeholder entries and TODO notes removed
*   User Interface meets requirements (5 points)
    *   Error messages are appropriate 
    *   Program has no hard-coded paths and functions when run from *any* directory
*   `area-titles.csv` is processed in accordance with requirements (15 points)
    *   File is read one line at a time
    *   Its data is stored into a dictionary
    *   Required FIPS areas are included; others are excluded
    *   File is closed after being read
*   The Annual Single File CSV is processed according to requirements (20 points)
    *   File is read one line at a time, and only one line of the file is stored in memory at a time
    *   Lines are skipped appropriately based on FIPS, industry and ownership codes
    *   Proper data conversion functions are employed (no `eval()` allowed!)
    *   File is closed after being read
*   The program finishes in a *reasonable* amount of time (5 points)
*   Report output meets customer's requirements (10 points)
    *   Source file `report.py` is left unchanged
    *   Program output matches provided examples
        *   Information appears in the correct sections of the report
        *   Correct counts and totals are provided
        *   FIPS areas are displayed as "County, State" and not as FIPS codes
    *   No extraneous output is printed to STDOUT (extra output printed to STDERR is permitted)


## Important Things to Watch Out For

0.  **100% penalty** your program imports any modules **except**:
    *   `sys`
    *   `time`
    *   `typing`
    *   modules in the starter code
    *   new modules you wrote on your own
1.  **100% penalty** your program uses the `csv` module.
    *   [Why this module is not on the approved list](./Requirements.md#can-i-use-pythons-csv-module)
2.  **100% point penalty** if external programs are called to do the work.
    *   Do not use `os.system()`, `subprocess`, `pipes` or similar features.
    *   This is a pure Python program, not a shell script that leverages external programs.
3.  **10 point penalty** an import statement fails due to misspelling or incorrect capitalization.
    *   **Windows users** make sure that the capitalization of your file names on GitLab matches your `import` statements!
4.  **10 point penalty** the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration
5.  **10 point penalty** repository's URL on GitLab does not follow the naming convention
6.  **10 point penalty** repository is not a clone of the starter code
7.  **10 point penalty** required files or directories are missing, renamed or not in their expected locations
8.  **10 point penalty** `.gitignore` is missing or corrupt; forbidden files or directories are present in repository.  If you accidentally commit a huge CSV file, ask the instructor for help.
