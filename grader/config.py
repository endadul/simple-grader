#========================
# Configuration file
#=======================

# Control variables
#-----------------
# Run each testcase for the specified interval
TIMEOUT = 10 # in seconds

#
# A general bash script that contains the specific
# command to run the test program
# 
PROG = "run.sh" 

# Define test cases 
testcases = {}

# Testcase template
# testcases['test1'] = {
# 	'name':'Test1', 
# 	'summary': 'Testing basic functionality',
# 	'score':'20',
# 	'input':"testcases/test1.in", 
# 	'output':"logs/test1.out",
# 	'expected': "testcases/test1.ex"
# 	}

testcases['test1'] = {
	'name':'Test1', 
	'summary': 'Testing basic functionality',
	'score':'20',
	'input':"testcases/test1.in", 
	'output':"logs/test1.out",
	'expected': "testcases/test1.ex"
	}


