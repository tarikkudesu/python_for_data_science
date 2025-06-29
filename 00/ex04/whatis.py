import sys

assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
if (len(sys.argv) == 2 and int(sys.argv[1]) % 2 == 0):
	assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"
	print("I'm Even.")
elif (len(sys.argv) == 2):
	print("I'm Odd.")
