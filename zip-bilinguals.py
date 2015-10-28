#!/usr/bin/env python

import os, sys, argparse

if __name__ == "__main__":
  ap = argparse.ArgumentParser()
  ap.add_argument("file1")
  ap.add_argument("file2")
  args = ap.parse_args()

  file1, file2 = map(open, [args.file1, args.file2])

  while True:
    line1, line2 = map(lambda x: x.readline(), [file1, file2])
    if not line1 or not line2:
      break
    print "%s ||| %s" % (line1.strip(), line2.strip())