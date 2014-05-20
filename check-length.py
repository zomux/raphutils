import sys, os

if __name__ == "__main__":

  if len(sys.argv) != 3:
    print "python check-length.py [corpus] [length]"
    raise SystemExit

  _, corpus, length = sys.argv
  length = int(length)

  counter = 0

  for line in open(corpus).xreadlines():
    if len(line.strip().split(" ")) >= length:
      counter += 1

  print counter
