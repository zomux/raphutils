import sys, os

if len(sys.argv) != 3:
  print "python bleu.py [reference] [result]"
  raise SystemExit

_, ref, result = sys.argv

if not os.path.exists("/tmp/bleu"):
  os.mkdir("/tmp/bleu")

tmpPathRef = "/tmp/bleu/" + str(hash(ref))
tmpPathResult = "/tmp/bleu/" + str(hash(result))

open(tmpPathRef, "w").write(open(ref).read().strip() + "\n")
open(tmpPathResult, "w").write(open(result).read().strip() + "\n")

print "LINES:", len(open(tmpPathRef).readlines()), len(open(tmpPathResult).readlines())

cmd = "~/apps/mosesdecoder/scripts/generic/multi-bleu.perl %s < %s" % (tmpPathRef, tmpPathResult)

print cmd
os.system(cmd)