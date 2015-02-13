plato
========

![The man himself](https://raw.githubusercontent.com/abreen/socrates/master/socrates.jpg)

`plato` is a Python program that was written to make the grading
process more efficient by automating the repetitive tasks ordinarily done
by human graders. 'plato' is a branch-off of socrates, a grading program
written by Alex Breen.
 
To this end, the program provides tools to run
pre-programmed *tests* defined by an instructor or the teaching staff
in a *criteria file*. The criteria file is a plain text file
that describes the required parts of a submission, and
any number of tests designed by the instructor or teaching staff.
Reading this file, `plato` will determine which parts of a submission
are present, and run the tests for the parts of a submission that
are present. Missing parts of a submission or failed tests constitute
the deductions for a particular submission. When `plato` has run
all the tests it can, it writes a *grade file* to the student's
submission directory.

Obviously, there are some cases in which a test for `plato` cannot
be designed. For example, examining a solution for proper code style
or appropriate documentation must be done by a human grader. For this
task, the `review` test was created. When `plato` finds a `review`
test, it pauses the grading to allow the human grader to review a part
of the submission and take deductions, if necessary.

The ultimate goal is to automate as many tests as possible. However,
`plato` is a relatively new tool, and currently only has support for
a few kinds of assignments.

For much more information, see our [wiki on GitHub][wiki].


[wiki]: https://github.com/abreen/socrates/wiki/
