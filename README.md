# simple-grader
A simple and configurable grading software to grade any interactive program.

## Assumptions
  - The assignment takes input from console (`STDIN`) and prints output to the console (`STDOUT`). Any error is printed to the `STDERR`.
  - The assignment runs in interactive mode that is it gives a prompt for user command
  - The assignment creates an executable with a common name (e.g., `prog`)
  - The assignment has a `Makefile` to build the executable


## Repository structure

  - `grader/` - Contains the grading program
  - `sample-assignment/` - A sample programming assignment (a stack implementation in C++) to be graded

## How to use it (Tutorial)

  - Download the git repo
  - Copy the directory `grader/` to `sample-assigment/` by typing

```
  $ cp -r grader/ sample-assignment/
```

  - Go to the `sample-assignment/grader` directory and then start garding
```  
    $ cd sample-assignment/grader
    $ make
```
  - The grader will generate output as follows (or similar)
```
bash build.sh
make[1]: Entering directory `/PATH_TO_YOUR_REPO/simple-grader/sample-assignment'
g++ -Wall -o stack-prog stack-driver.cc
make[1]: Leaving directory `/PATH_TO_YOUR_REPO/simple-grader/sample-assignment'
python grade.py
Testcase:  Test1
Generated report for sample-assignment

```
  - The `./grade_report.txt` is the grading report that contains several information such as 
    -  Test inputs
    -  Expected output
    -  The output generated by the assignment

## Tested platform

It's been tested on Linux (Ubuntu 14.04) with Python 2.7.3. It should work on other Linux version.
    
## How to configure the grader

  - Modify `grader/build.sh`
    - `build.sh` assumes the assignment has a `Makefile` and a simple `make` would build the executable
  - Modify `grader/run.sh`
    - Update `PROGRAM` variable with the common name of the executable program that you are going to grade e.g., `PROGRAM="the-name-of-assignment-executable"`
  - Modify `grader/config.py`
    - Cofiguration variables for the grader are listed in `config.py`. Each testcase information is also listed.
  - Add test cases to the grader
    - You can add as many test cases as required for your purpose to the `grader/testcases/` directory
      - `test1.in` - The input for the test case
      - `test1.ex` - The expected output
      - Update `config.py` accordingly



