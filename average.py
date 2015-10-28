#!/usr/bin/env python
import os, sys


if __name__ == '__main__':
  n = 0
  total = 0.0
  for l in sys.stdin.xreadlines():
    l = l.strip()
    total += float(l)
    n += 1

  print "average = ", total / n
