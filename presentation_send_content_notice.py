#!/usr/bin/python3

import csv;
import sys;
import time;
import smtplib;
import random;
import config;
from string import Template;
from getpass import getpass;
from email.mime.text import MIMEText

smtp_pass = getpass("Enter password for \'%s\': " % config.SMTP_user);

with open('texts/presentation_content.inc', 'r') as pres_content:
  badge_tmpl=Template(pres_content.read());


# This could probably be done more intelligently with better error checking
# Should probably set this up to ensure all entries are correct and sane
# and then send them out in bulk, rather than one at a time.
with open(sys.argv[1], 'r') as csvfile:
  csvlines=csv.DictReader(csvfile, delimiter=',');
  for row in csvlines:
    if row['Accepted'].lower() == "y":
      response = badge_tmpl.substitute(Name=row['Name'].split(' ')[0],
        Organizer_phone=config.Organizer_phone,
        Badge_meet=config.Badge_meet,
        Speaker_ops=config.Speaker_ops,
        Content_deadline=config.Content_deadline,
        Signature=config.Signature);
    elif row['Accepted'].lower() == "n":
      continue;
    else:
      print("Presentation title \'%s\' has invalid \'Accepted\' column!" % row['Title'])
      print("Not sending any email for this row or any further rows!")
      raise SystemExit


    print("_____________________________________________________________________________")
    print(response)
    print("_____________________________________________________________________________")

    question = input("Do you want to send the previous email to \'%s\'? (y/n): " % row['Email']);
    if question.lower() == "y":
      msg = MIMEText(response);
      msg['Subject'] = config.Email_subject + " CFP -- Content Request";
      msg['From'] = config.Email_from;
      msg['To'] = row['Email'];

      # This is set up for TLS, if another protocol is used then this may need
      # to be adjusted.
      send = smtplib.SMTP(config.SMTP_url, config.SMTP_port);
      send.ehlo();
      send.starttls();
      send.login(config.SMTP_user, smtp_pass);
      send.sendmail(msg['From'], msg['To'], msg.as_string());
      send.quit();
    else:
      print("Skipped sending this email!")
      time.sleep(2);
