from __future__ import division

f_handle = open('files/results.txt', 'r')
lines = f_handle.readlines()
f_handle.close()

confMatrix = [[0 for x in xrange(13)] for x in xrange(13)]
p = [0.0 for x in xrange(13)]
r = [0.0 for x in xrange(13)]
f = [0.0 for x in xrange(13)]
predictCount = [0 for x in xrange(13)]
actualCount = [0 for x in xrange(13)]
pAll = 0.0
rAll = 0.0
fAll = 0.0
countAll = 0

#preprocessing for scores
f1 = open('scores.txt', 'w')
f2 = open('confMatrix.txt', 'w')
for i, line in enumerate(lines):
    predict =  int(line)
    countAll += 1
    predictCount[predict] += 1
    
    label = 0
    if i <= 10: # BRK
        label = 1
    elif i <= 54: # BRM
        label = 2
    elif i <= 941: # GRW
        label = 3
    elif i <= 1014: # LRM
        label = 4
    elif i <= 1060: # LRR
        label = 5
    elif i <= 1063: # MCR
        label = 6
    elif i <= 1078: # ROR
        label = 7
    elif i <= 1105: # RRM
        label = 8
    elif i <= 1163: # RUM
        label = 9
    elif i <= 1290: # SQK
        label = 10
    elif i <= 1303: # SQL
        label = 11
    elif i <= 1348: # TMP
        label = 12
    confMatrix[label][predict] += 1
    actualCount[label] += 1

#calculate precision, recall, and f-scores
for i in range(1,13):
    p[i] = confMatrix[i][i]
    r[i] = confMatrix[i][i]
for i in range(1,13):
   r[i] /= actualCount[i]
   if predictCount[i] == 0:
        p[i] = -1
        f[i] = -1
   else:
       p[i] /= predictCount[i]
       f[i] = 2*p[i]*r[i]/(p[i]+r[i])

calls = ["BRK", "BRM", "GRW", "LRM", "LRR", "MCR", "ROR", "RRM", "RUM", "SQK", "SQL", "TMP"]

#write confusion matrix to file
print >> f2, "\t"+"\t".join(calls)
for i in range(1,13):
    f2.write(calls[i-1])
    for k in range(1,13):
        f2.write("\t"+str(confMatrix[i][k]))
    f2.write("\n")

#write precision, recall, f scores to file
print >> f1, "\t"+"\t\t".join(calls)
f1.write("P")
for i in range(1,13):
    f1.write("\t"+'%.3f' % p[i])
f1.write("\n\n")
f1.write("R")
for i in range(1,13):
    f1.write("\t"+'%.3f' % r[i])
f1.write("\n\n")
f1.write("F")
for i in range(1,13):
    f1.write("\t"+'%.3f' % f[i])
f1.write("\n\n*score of -1 means 0 classified as the call type")

f1.close()
f2.close()
