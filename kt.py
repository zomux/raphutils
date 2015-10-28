#!/usr/bin/python
#kendall's tau, tei, 2013.07.27

import sys, os, codecs

file = codecs.open (sys.argv [1], "r", "utf-8")
lines = file.read ().split ("\n") [:-1]
file.close ()
print "lines : ", len (lines)
#lines = lines [:100000]

#collect tau
taus = []
def tau (pairs) :
	global taus
	all = 0.5 * len (pairs) * (len (pairs)-1)
	con, tie, dis = 0, 0, 0
	for i in range (len (pairs)) :
		for j in range (i+1, len (pairs)) :
			flag = (int (pairs [i][0]) - int (pairs [j][0])) * (int (pairs [i][1]) - int (pairs [j][1]))
			if   flag  > 0 : con += 1
			elif flag == 0 : tie += 1
			elif flag  < 0 : dis += 1
			else : assert False
	assert con + tie + dis == all
	if all != 0 : taus.append (((con/all)*2-1, ((con+tie)/all)*2-1))
	else : print "\n!!! a sentence without any aligned pair ..."
	#if len (taus) % 1000 == 0 : print len (taus), "...\r",
	print len (taus), "...\r",
for line in lines : tau ([pair.split ("-") for pair in line.strip (" \n\r").split ()])

#get distribution of tau
scale = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01]
distr = [[0, 0] for x in range (20)]
total = [0, 0]
aver  = [0, 0]
for strict, loose in taus :
	aver [0] += strict
	aver [1] += loose
	for i in range (20) : 
		if scale [i] <= strict < scale [i+1] : distr [i][0] += 1; break
	for i in range (20) : 
		if scale [i] <= loose  < scale [i+1] : distr [i][1] += 1; break
for i in range (len (distr)) : distr [i][0], distr [i][1] = distr [i][0] / (len (taus)+0.0), distr [i][1] / (len (taus)+0.0)
for i in range (len (distr)) : total [0] += distr [i][0]; total [1] += distr [i][1]
aver [0], aver [1] = aver [0] / len (taus), aver [1] / len (taus)

#print blablablahhh
print "\ntau distr.\tstrict\tloose"
print "------------------------------"
for i in range (20) : print "%+.1f ~ %+.1f\t%.3f\t%.3f"%(scale [i], scale [i+1], distr [i][0], distr [i][1])
print "------------------------------"
print "%s\t%.3f\t%.3f"%("tau total", total [0], total [1])
print "%s\t%.3f\t%.3f"%("tau average", aver [0], aver [1])
print	
