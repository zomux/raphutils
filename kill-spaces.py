import sys, os

if len(sys.argv) != 2:
  print "python kill-spaces.py [filename]"
  raise SystemExit

_, filename = sys.argv
print open(filename).read().replace(" ", ""),
