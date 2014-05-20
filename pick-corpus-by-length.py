import sys, os

MAX = 100

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print "python pick-corpus-by-length.py [corpus] [min-length] [max-length]"
    raise SystemExit

  _, corpus, minLength, maxLength = sys.argv
  minLength, maxLength = map(int, [minLength, maxLength])

  counter = 0

  for line in open(corpus).xreadlines():
    line = line.strip()
    wordCount = line.count(" ") + 1
    if wordCount >= minLength and wordCount <= maxLength:
      print line
      counter += 1
      if counter == MAX:
        break
