# CS 1440 Assignment 3: Big Data Processing - Shell Tutor


*   [Quickstart](#quickstart)
*   [Submission Instructions](#submission-instructions)
*   [Lesson Contents](#lesson-contents)
*   [Hints](#hints)
*   [Reporting Bugs](#reporting-bugs)


## Quickstart

*In the code examples below a dollar sign `$` represents the shell prompt.  This is to distinguish commands that you will input from their output. Do not type the `$` when you run these commands yourself.*

Enter the `shell-tutor` directory and execute one of the `.sh` files from Bash or Zsh:

```
$ cd shell-tutor

$ ./0-tagging.sh

Git Tag Syntax
Tutor:
Tutor: In this lesson you will learn how to
Tutor:
Tutor: * Use the basic command syntax and concepts for git tagging
Tutor: * Add new tags to commits
Tutor: * Remove tags from commits
Tutor: * Manage tags on remote repositories
```

**NOTE FOR UBUNTU USERS:** Your shell's default `sh` is not compatible with the shell tutor.  Run lessons with `bash ./0-shortcuts.sh` instead of `./0-shortcuts.sh`.


## Submission Instructions

At the end of a lesson **do not close the terminal** until you see the message `You worked on this lesson for ...`.

After completing the lessons run `bash make-certificate.sh` to create your certificate of completion.  `git add` and `git commit` the certificate in this directory.


## Lesson Contents

*   `0-tagging.sh`
    * Learn the basic command syntax and concepts for git tagging
    * Add new tags to commits
    * Remove tags from commits
    * Manage tags on remote repositories
*   `1-project-tags.sh`
    * Add development phase tags to commits in a project
    * Push tags to remote repository


## Hints

*   Interact with the tutor through the `tutor` command.
    *   When you get lost or forget what to do next, run `tutor hint`.
*   You can leave the tutorial early by exiting the shell.  There are many
    ways to do this:
    *   The `exit` command
    *   The `tutor quit` command
    *   Type the End-Of-File character (EOF) `Ctrl-D`
*   Lessons are designed to be brief; the average student will finish a lesson
    in 20 minutes.  If you are stuck longer than 20 minutes you can seek help
    from the instructor, TAs or CS Coaching Center.


## Reporting Bugs

*   When you encounter a problem with a lesson, please send a bug report so I can fix it
    *   Run `tutor bug` 
        *   Scroll up a before the problem started and copy the text on your terminal, including these details:
        -   Which lesson you are running
        -   Which step of the lesson you were on
        -   The instructions for that step
        -   The command you ran
        -   The erroneous output
        -   The output of the `tutor bug` command
*   Send this text to me in an email: `erik DOT falor AT usu DOT edu`
    *   **CC Jaxton Winder as well** : `jaxton DOT winder AT usu DOT edu`
    *   **Do not** send screenshots; plain text is much easier to work with
