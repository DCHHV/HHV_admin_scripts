#!/usr/bin/python3

import csv;
import sys;
import time;
import smtplib;
import config;
from string import Template;
from getpass import getpass;
from email.mime.text import MIMEText

smtp_pass = getpass("Enter password for \'%s\': " % config.SMTP_user);

with open('texts/presentation_accepted.inc', 'r') as pres_accept:
  accepted_tmpl=Template(pres_accept.read());

with open('texts/presentation_rejected.inc', 'r') as pres_reject:
  rejected_tmpl=Template(pres_reject.read());

# This could probably be done more intelligently with better error checking
# Should probably set this up to ensure all entries are correct and sane
# and then send them out in bulk, rather than one at a time.
with open(sys.argv[1], 'r') as csvfile:
  csvlines=csv.DictReader(csvfile, delimiter=',');
  for row in csvlines:
    if row['Accepted'].lower() == "y":
      response = accepted_tmpl.substitute(Name=row['Name'].split(' ')[0],
        Title=row['Title'], Abstract=row['Abstract'], Bio=row['Bio'],
        DC_num=config.DC_num, DC_days=config.DC_days,
        DC_floormapurl=config.DC_floormapurl,
        Additional_Comments=row['Additional_Comments'],
        Response_deadline=config.Response_deadline,
        Content_deadline=config.Content_deadline,
        Signature=config.Signature);
    elif row['Accepted'].lower() == "n":
      response = rejected_tmpl.substitute(Name=row['Name'].split(' ')[0],
      Title=row['Title'], DC_num=config.DC_num,
      Signature=config.Signature)
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
      msg['Subject'] = config.Email_subject + " CFP Response";
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
