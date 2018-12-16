#!/usr/bin/python

# At this time, does not actually print chronologically

import sys;
import csv;

with open(sys.argv[1], 'r') as csvfile:
  csvlines=csv.DictReader(csvfile, delimiter=',');
  print "________________________________________________________________________________"
  for row in csvlines:
    name = row['Name']; #, additional names
    addnames = row['Additional Names'];
    datetime = row['Time'];
    title = row['Title'];
    abstract = row['Abstract'];
    bio = row['Bio'];
    print "NAME:";
    if addnames:
      print("%s, %s\n" % (name, addnames));
    else:
      print name, "\n";
    print "DATE & TIME:"
    print datetime, "\n";
    print "TITLE:"
    print title, "\n";
    print "ABSTRACT:"
    print abstract, "\n";
    print "BIO:"
    print bio, "\n";
    print "________________________________________________________________________________"
   
