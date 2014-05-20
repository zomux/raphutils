import sys

for line in sys.stdin.readlines():
  text = open(line.strip()).read().strip()
  if "\n" not in text:
    print text
    print "---"
