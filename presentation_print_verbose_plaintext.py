#!/usr/bin/python

# Simple script to transform CSV from goog forms to a more organized plaintext for
# evaluation and commenting. Contains more verbose information about each
# presentation that would be more than DEF CON would likely want.
#
# Output fields include:
#   Name(s) of presenter(s)
#   Social media accounts
#   Website for presenter(s) or presentation
#   Title of presentation
#   Abstract
#   Outline
#   Speaker Bio

import csv;
import sys;

with open(sys.argv[1], 'r') as csvfile:
  csvlines=csv.DictReader(csvfile, delimiter=',');
  print "______________________________________________________________________________"
  for row in csvlines:
    name = row['Name'];
    addnames = row['Additional Names'];
    social_media = row['Social Media'];
    website = row['Website'];
    title = row['Title'];
    abstract = row['Abstract'];
    outline = row['Outline'];
    bio = row['Bio'];
    print "NAME:";
    if addnames:
      print("%s, %s\n" % (name, addnames));
    else:
      print name, "\n";
    print "SOCIAL MEDIA:"
    print social_media, "\n";
    print "WEBSITE:"
    print website, "\n";
    print "TITLE:"
    print title, "\n";
    print "ABSTRACT:"
    print abstract, "\n";
    print "DETAILED OUTLINE:"
    print outline, "\n";
    print "BIO:"
    print bio, "\n";
    print "______________________________________________________________________________"
   
