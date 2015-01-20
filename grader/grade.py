#!/usr/bin/env python
#
# A simple grader program
# 
# Author: Endadul Hoque <mhoque@purdue.edu>
#
# This simple grader program does not compare 
# test results using 'diff'. It simply generates
# a test report that contains
#   - Each test case info
#   - Corresponding test inputs
#   - Expected outputs
#   - Program generated outputs
# 

import argparse, os, sys, random, errno, signal, time
from subprocess import Popen, PIPE
from config import testcases
from config import TIMEOUT
from config import PROG

BASEDIR = os.path.dirname(os.path.abspath(__file__))


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

def reset_alarm():
    signal.alarm(0)
    return

def set_alarm(timeout=TIMEOUT):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout) # in sec
    return




def get_process_children(pid):
    p = Popen('ps --no-headers -o pid --ppid %d' % pid, shell = True,
              stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()
    return [int(p) for p in stdout.split()]

def kill_all(pid):
    pids = [pid]
    pids.extend(get_process_children(pid))
    for p in pids:
        # process might have died before getting to this line
        # so wrap to avoid OSError: no such process
        try: 
            os.kill(p, signal.SIGKILL)
        except OSError:
            pass


def run_test(test):    
    mkdir_p(os.path.dirname(test['output']))    
    out = ""
    err = ""
    # command: stdbuf -o0 bash run.sh
    inputs = "".join(open(test['input']).readlines())
    cmd = ['stdbuf', '-o0', 'bash', PROG]       
    print "Testcase: ", test['name']
    
    
    try:
        set_alarm()
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        try:
            for inp in inputs.split("\n"):
                if proc.poll() is None: # alive
                    proc.stdin.write("{}\n".format(inp))
                    time.sleep(0.1) 

            while proc.poll() is None: # not dead yet                    
                line = proc.stdout.readline()
                if line:
                    out += line + "\n"              
                    #print "STDOUT: " + line.strip()
            reset_alarm()
            err = proc.stderr.readlines()
            out = proc.stdout.readlines()
            if len(err) > 0:
              err = "".join(err)
            if len(out) > 0:
              out = "".join(out)

        except Alarm:
            #print "Oops, timeout!"
            pass

        kill_all(proc.pid)

        if proc.returncode and proc.returncode != 0:
            print"Process exited with code", proc.returncode
            if err and len(err) > 0:
                err += "\nProcess exited with code " + str(proc.returncode)
            else:
                err = "Process exited with code " + str(proc.returncode)

        log_test_result(test, inputs, out, err)       
            
    except OSError as exc:
        print "Error :" , exc
        raise
    return


def log_test_result(test_item, input_text, output_text, error_text=None):
    with open(test_item['output'], 'w') as fout:        
        fout.write("Test case: " + test_item['name'] + "\n")
        fout.write("Summary: " + test_item['summary'] + "\n")
        fout.write("Score: " + test_item['score'] + "\n")        
        
        # inputs
        fout.write("\nGiven input: \n") # + input_text + "\n")
        count = 1
        for ll in input_text.split("\n"):
            if len(ll) > 0:
                fout.write("Command " + str(count) + ": " + ll.strip() + "\n")
                count += 1

        # expected output
        try:
            fout.write("\nExpected output: \n" +             
                "".join(open(test_item['expected']).readlines()))
        except IOError as ex:            
            pass

        # Stdout text
        if output_text:
            fout.write("\n\nGenerated output: \n")            
            for ll in output_text.split("\n"):
                if len(ll) > 0:
                    fout.write(ll.strip() + "\n")                     

        # Stderr text
        if error_text:
            fout.write("\nGenerated error: \n" + error_text + "\n")

    return


def student_name():
    return BASEDIR.split("/")[-2]

def generate_report(test_items):
    test_case_separator = "\n#" + "=" * 50 + "#\n"
    student = student_name()
    with open('grade_report.txt', 'w') as fout:        
        fout.write('Student: ' + student + "\n")
        fout.write("Current directory: {}\n".format(BASEDIR))
        fout.write('*'*60 + "\n\n")

        try:
            for key in sorted(test_items.keys()):
                item = test_items[key]
                fout.write(test_case_separator)
                lines = "".join(open(item['output'], 'r').readlines())
                fout.write(lines)
                fout.write(test_case_separator)

            fout.write("\n\nTotal Score: \n")            

        except IOError as io:
            print "Error occurred while processing: ", item['output']
            raise        
    print "Generated report for", student
    return

def start(testcases):
    for name in sorted(testcases.keys()):
        run_test(testcases[name])
    generate_report(testcases)
    return

if __name__ == '__main__':
    start(testcases)

