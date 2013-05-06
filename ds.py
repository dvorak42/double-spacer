#!/usr/bin/python
import sys

f = open(sys.argv[1])
s = f.read()
s2 = s.replace("\n", "\n\n")
f.close()
f = open(sys.argv[1], 'w')
f.write(s2)
f.close()
