import sys
import random

n = int(sys.argv[1])

for i in range(n):
	for j in range(n):
		if i == j:
			print 0,
		else:
			print random.randrange(1.0, 20.0),
	print
