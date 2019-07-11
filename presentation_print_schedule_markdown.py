#!/usr/bin/python

import csv;
import sys;

with open(sys.argv[1], 'r') as csvfile:
  # Sort CSV file in order by "Time" column.
  csvlines=csv.DictReader(csvfile, delimiter=',');
  sortedcsv=sorted(csvlines, key=lambda row: row['Time'], reverse=False);

  # Start by printing basic schedule links, these can go in to tables and
  # are already markdown formated for website use. Not perfect, but it
  # makes the schedule page layout process a lot faster. Some of the
  # inline links will still need to be cleaned up if they have special
  # characters or other things.
  for row in sortedcsv:
    if row['Accepted'].lower() != "n":
      print("%s" % (row['Time']));
      print("%s - [%s](#%s)" % (row['Format'], row['Title'].title(), row['Title'].replace(' ','-').lower()));
      
  print("");

  # Start with basic markdown formatting outlines for the page
  print("## Talk/Workshop Details");
  print("* * *");
  for row in sortedcsv:
    if row['Accepted'].lower() == "n":
      continue;
    elif row['Accepted'].lower() != "y":
      print("Presentation title \'%s\' has invalid \'Accepted\' column!" % (row['Title']));
      print("Not sending any email for this row or any further rows!");
      raise SystemExit


    # Output information for each talk
    print("### %s" % (row['Title'].title()));
    if row['Additional Names']:
      print("%s %s" % (row['Name'], row['Additional Names']));
    else:
      print("%s" % (row['Name']));
    print("#### Abstract");
    print("%s" % (row['Abstract']));
    print("#### Bio");
    print("%s" % (row['Bio']));
    print("* * *");
      
#    print"_____________________________________________________________________________"
#    print response
#    print"_____________________________________________________________________________"

#    question = raw_input("Do you want to send the previous email to \'%s\'? (y/n): " % row['Email']);
#    if question.lower() == "y":
#      msg = MIMEText(response);
#      msg['Subject'] = config.Email_subject + " CFP Response";
#      msg['From'] = config.Email_from;
#      msg['To'] = row['Email'];

      # This is set up for TLS, if another protocol is used then this may need
      # to be adjusted.
#      send = smtplib.SMTP(config.SMTP_url, config.SMTP_port);
#      send.ehlo();
#      send.starttls();
#      send.login(config.SMTP_user, smtp_pass);
#      send.sendmail(msg['From'], msg['To'], msg.as_string());
 #     send.quit();
#    else:
#      print "Skipped sending this email!";
#      time.sleep(2);
