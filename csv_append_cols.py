#!/usr/bin/python

import csv;
import sys;

with open(sys.argv[1], 'r') as csvread:
    reader = csv.reader(csvread)

    all = []
    row = reader.next()
    row.append(sys.argv[2])
    all.append(row)

    for row in reader:
        row.append(sys.argv[3])
        all.append(row)

with open(sys.argv[1], 'w') as csvwrite:
  writer = csv.writer(csvwrite, lineterminator='\n')
  writer.writerows(all)

