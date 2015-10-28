
import sys, os, codecs

#collect tau
taus = []

for line in sys.stdin.xreadlines():
	taus.append(float(line.strip()))

#get distribution of tau
scale = [-1.01, -0.9999, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.01]
distr = [0 for x in range (len(scale)-1)]
total = 0
aver  = 0
for tau in taus :
	aver  += tau
	for i in range (len(scale)-1) :
		if scale [i] <= tau < scale [i+1] : distr [i] += 1; break
for i in range (len (distr)) : distr [i] = distr [i] / (len (taus)+0.0)
for i in range (len (distr)) : total  += distr [i]
aver  = aver / len (taus)

print "\ntau\ttau"
print "------------------------------"
for i in range (len(scale)-1) : print "%+.1f ~ %+.1f;%.3f"%(scale [i], scale [i+1], distr [i])
print "------------------------------"
print "%s\t%.3f"%("total", total )
print "%s\t%.3f"%("aver", aver )
print
