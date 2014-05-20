#!/usr/bin/env python
import sys, os

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "split-bilinguals.py [output-prefix] < [bilingual-file]"
    print "Every line in bilingual file should be formatted as:"
    print "[English Side] ||| [Japanese Side]"
    raise SystemExit

  _, prefix = sys.argv

  enFile, jaFile = [open(filename, "w") for filename in ["%s.en" % prefix, "%s.ja" % prefix]]
  for line in sys.stdin.xreadlines():
    line = line.strip()
    if not line:
      continue
    pair = line.split(" ||| ")
    en = pair[-2]; ja = pair[-1]
    enFile.write(en + "\n")
    jaFile.write(ja + "\n")
