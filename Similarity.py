l = sc.textFile("/user/cloudera/test/dataset.txt")

lTmp = l.map(lambda x: (x.split(",")[0].replace('"',''), x.split(",")[1:]))

lTmp = lTmp.map(lambda x: (x[0], map(int, x[1])))

lCombined = lTmp.cartesian(lTmp)


import numpy
from scipy import spatial

output = lCombined.map(lambda x: x[0][0] + ";" + x[1][0] + ";" + str(1 - spatial.distance.cosine(x[0][1], x[1][1])))


# Salvo l'output
output.saveAsTextFile('/user/cloudera/test/outputSimilarity')
