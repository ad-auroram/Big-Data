# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
    
Write a python code that takes data from the Bureau of Labor Statistics' Quarterly Census of Employment and Wages (formatted in a CSV file)
and summarizes it in a nice easy to read report.

*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

A good solution will pass any provided unit tests, as well as any other test cases I design. It will be able to run through all the provided data and identify the 
relevant pieces of info.

***Things I know:***
  * How to open and read files
  * Making a dictionary (probably)
  * Finding specific characters/values/strings within strings

***Things I don't know yet:***
* splitting up strings the way I want them to be (lines in the dictionary)
* don't really know much at all about dictionaries other than what we did in class


*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.

The program uses a CSV file of the data, the output will take the form of a formatted report with a print() statement. 
Said statement is in a function that takes info from other modules (industry_data).
*   [ ] List the algorithms that will be used (but don't write them yet).

A dictionary containing the relevant records (based on FIPS codes) will be the main part.

*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

### util.py
* record_matches_fips
  * check record for valid FIPS areas
```commandline
if record is in areas:
    return true
```

* record_is_all_industries
  * check if record is about all industries
```commandline
if all industries code in records:
    return true
```

* record_is_software_industry
  * check if record is about software industry
```commandline
if software industry code in records:
    return true
```

* get_fips
  * take fips code from record
```commandline
list = split record along commas
return list[0]
```

* get_estabs
  * take average quarterly establishment counts
```commandline
list = split record along commas
return list[9]
```

* get_emplvl
  * take annual average of monthly employment levels
```commandline
list = split record along commas
return list[10]
```

* get_wages
  * take total of 4 quarterly wage levels
```commandline
list = split record along commas
return list[11]
```

### area_titles.py
* area_titles_to_dict
  * take the file area-titles and convert it to a dictionary
```commandline
create dictionary areas
file = open(dirname/area-titles.csv)
file.readline
for line in file
    split into 2 fields
    if fips code is valid (should be numerical and not end with 000)
        add to dictionary
close file
return areas
```

### industry_data.py
* all attributes under __init__ initialized to 0 or ""
```commandline
num_areas = 0
total_annual_wages = 0
max_annual_wage = ""
total_estab = 0
max_estab = ""
total_empl = 0
max_empl = ""
#any strings become lists later
```
* add_record
  * adds data from a record to summary statistics
```commandline
num_areas +=1
add total annual wages
track area with max annual wages
total_estab += estab from record
track area with max_estab
total_empl += empl from record
track area with max_empl
```

### big_data.py
print usage message and exit if directory name isn't given
call area_titles_to_dict with given directory (let it crash on its own if it fails)
get data from 2022.annual.singlefile.csv and put it in the report dictionary
```commandline
for line in file
    if fips in areas
        add record to report
```

## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.

When returning values in util.py, I didn't realize I'd have to strip quotation marks off of strings, and I kept
forgetting to convert things to int that needed converting.

For area_titles, I learned about the endswith() function to check for statewide statistics and exclude them. 
Once I figured that out, I referenced the dictionary demonstration in class and modeled this one after it, and it was smooth sailing from there.

industry_data.py originally had a lot more calls to util functions, but I replaced them by 
defining variables with them at the beginning of the method, so then they'd be called once rather than multiple times.

I felt I had a good idea of how to approach big_data.py, but ran into a block when I couldn't quite remember how to call instances of a class in Python. 
I reviewed more and I think it's all good now. I'll have to change more values I think, but I'll run some tests to see where the data is coming from/going for sure first.

*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.

### Test 1: Unit Tests
```commandline
$ python run_tests.py
```
* Expected: should pass all tests
#### Result: Pass

### Test 2: No directory given
```
$ python src/big_data.py
```
* Expected: should return an error and exit
#### Results: Pass

### Test 3: DC_Complete
```commandline
$ python src/big_data.py data/DC_complete
```
* followed directions on the requirements page to create statistics for DC.
* Output should match output.txt
#### Result: realized I forgot to delete print statements. Forgot to split line before passing to methods.
#### Take 2: Passed expect for quotation marks around location name.
#### Take 3: Passed.

### Test 4: Invalid directory
```commandline
$ python src/big_data.py data/boo
```
* Expected: should return a "no such file or directory" error
#### Result: Passed

### Test 5: Utah reversed
```commandline
$ python src/big_data.py data/UT_reversed
```
* Followed directions in README to create dataset
* Output should match output.txt
#### Result: Passed

### Test 6: USA_full
```commandline
$ python src/big_data.py data/USA_full
```
* Expected: Output should match output.txt. The benchmark test says it should finish in under 18.28 seconds on my computer. 
#### Result: Passed! (in 6.4 seconds)

## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [x] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [x] Your repository is pushed to GitLab.
*   [x] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    
    I forgot tags had a different command to be pushed, whoops. They're all there now.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [x] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
