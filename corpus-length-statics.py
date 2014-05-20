import sys, os

def build_length_list(filename):
  lengthList = []
  for line in open(corpus).xreadlines():
    lengthList.append(len(line.strip().split(" ")))
  return lengthList

def count_length_in_list(lengthList, maxLength = 0, minLength = 0):
  if maxLength:
    ret = len([x for x in lengthList if x <= maxLength])
    print "maxLength=%d: %d (%.2f%%)" % (maxLength, ret, float(ret)*100/len(lengthList))
    return ret
  elif minLength:
    ret = len([x for x in lengthList if x >= minLength])
    print "minLength=%d: %d (%.2f%%)" % (minLength, ret, float(ret)*100/len(lengthList))
    return ret
  else:
    return None

if __name__ == "__main__":

  if len(sys.argv) != 2:
    print "%s [corpus]" % sys.argv[0]
    raise SystemExit

  _, corpus = sys.argv
  
  lengthList = build_length_list(corpus)

  print "ALL:", len(lengthList)

  count_length_in_list(lengthList, maxLength=5)
  count_length_in_list(lengthList, minLength=5)
  count_length_in_list(lengthList, minLength=8)
  count_length_in_list(lengthList, minLength=10)
  count_length_in_list(lengthList, minLength=20)
  count_length_in_list(lengthList, minLength=30)
  count_length_in_list(lengthList, minLength=80)
