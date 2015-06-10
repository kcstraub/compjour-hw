import sys
import csv
import operator

reader = csv.reader(open("10.csv"), delimiter=";")

from operator import itemgetter
sortedlist = sorted(reader, key=operator.itemgetter(16), reverse=True)