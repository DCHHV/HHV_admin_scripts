#!/usr/bin/python

import csv;
import sys;
import time;
import smtplib;
import config;
from string import Template;
from getpass import getpass;
from email.mime.text import MIMEText

smtp_pass = getpass("Enter password for \'%s\': " % config.SMTP_user);

with open('texts/guest_invitation.inc', 'r') as guest_invite:
  invite_tmpl=Template(guest_invite.read());

# This could probably be done more intelligently with better error checking
# Should probably set this up to ensure all entries are correct and sane
# and then send them out in bulk, rather than one at a time.
with open(sys.argv[1], 'r') as csvfile:
  csvlines=csv.DictReader(csvfile, delimiter=',');
  for row in csvlines:
    if row['Blacklist'].lower() == "n":
      response = invite_tmpl.substitute(Name=row['Name'].split(' ')[0],
        CFP_link='https://dchhv.org/CFP.html');
    elif row['Blacklist'].lower() == "y":
      print "Skipping \'%s\' as they have been removed from the active contact list!" % row['Name'];
      raise SystemExit
    else:
      print "\'%s\' has invalid \'Blacklisted\' column!" % row['Name'];
      print "Not sending any email for this row or any further rows!"
      raise SystemExit


    print"_____________________________________________________________________________"
    print response
    print"_____________________________________________________________________________"

    question = raw_input("Do you want to send the previous email to \'%s\'? (y/n): " % row['Email']);
    if question.lower() == "y":
      msg = MIMEText(response);
      msg['Subject'] = config.Email_subject + " CFP Invitation";
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
      print "Skipped sending this email!";
      time.sleep(2);
