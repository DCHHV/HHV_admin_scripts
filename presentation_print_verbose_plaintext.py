#!/usr/bin/env python3

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
  print("______________________________________________________________________________")
  for row in csvlines:
    name = row['Name'];
    addnames = row['Additional Names'];
    social_media = row['Social Media'];
    website = row['Website'];
    title = row['Title'];
    abstract = row['Abstract'];
    outline = row['Outline'];
    bio = row['Bio'];
    print("NAME:");
    if addnames:
      print("%s, %s\n" % (name, addnames));
    else:
      print("%s\n" % name);
    print("SOCIAL MEDIA:")
    print("%s\n" % social_media);
    print("WEBSITE:")
    print("%s\n" % website);
    print("TITLE:")
    print("%s\n" % title);
    print("ABSTRACT:")
    print("%s\n" % abstract);
    print("DETAILED OUTLINE:")
    print("%s\n" % outline);
    print("BIO:")
    print("%s\n" % bio);
    print("______________________________________________________________________________")
   
