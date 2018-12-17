# Administrative scripts for the HHV to mostly deal with the CFP process
Created with resources borrowed from: https://bridgetkromhout.com/blog/tl-dr-your-talk-is-accepted/
Which is a great resource for handling CFP responses and outlines the information that could be needed.


## About
Written mostly in python, these are a set of scripts to take CSV files of CFP information mangle them in to different output formats. These formats can be used by the CFP review team, AV team, etc. There are also scripts that will send off emails to CFP applications, for accepting/rejecting the presentation, sending out schedule information, and offering DEF CON human badges in the event that we are able to do so.

In the texts/ folder are a handful of .inc files that rely on string substitution to fill in the gaps. These substitutions are pulled from config.py as well as the CSV file passed to a specific script. All of the scripts will iterate through the rows of the CSV file and process on one row at a time.

Currently, there is practically no error checking with any kind of grace. We are mostly hardware engineers and python is not our primary language.


## Usage
### Config
The "config_tmpl.py" file needs to be copied to "config.py" and then all of the blanks filled in. That file contains comments to give a brief explanation of each variable. Scripts that make use of this config will import config.py.

### CSV file
The scripts expect a few specific column names in a CSV file. The default used is:
"Name","Email","Twitter","Website","Additional Names","Title","Abstract","Outline","Bio","Outline","Accepted","Time"

### Print scripts
There are two scripts that print out CSV file information in a human readable format.

`./presentation_print_brief_plaintext.py file.csv`

Prints:

```
________________________________________________________________________________
NAME:
<Names of presenters, uses "Additional Names" if not null>

DATE & TIME:
<Date and time of presentation>

TITLE:
<Title of presentation>

ABSTRACT:
<Abstract of presentation>

BIO:
<Bio of presenter(s)>
________________________________________________________________________________
```

`./presentation_print_verbose_plaintext.py file.csv`

Prints:

```
________________________________________________________________________________
NAME:
<Names of presenters, uses "Additional Names" if not null>

TWITTER:
<Twitter handle of presenter(s)>

WEBSITE:
<Website of presenter(s) or 

TITLE:
<Title of presentation>

ABSTRACT:
<Abstract of presentation>

DETAILED OUTLINE:
<Detailed outline of presentation>

BIO:
<Bio of presenter(s)>
________________________________________________________________________________
```


### Email scripts
There are three scripts that are used to email CFP applicants various pieces of information. 
These include the initial accept/reject email, notice of the presentation being scheduled, and an offer of a DEF CON human badge.

`./presentation_send_response_email.py file.csv`

Sends accept/reject email to each presenter, uses "texts/presentation_accepted.inc" and "texts/presentation_rejected.inc" files as the main body

`./presentation_send_scheduled_email.py file.csv`

Sends notice to each accpeted presentation that their presentation has been scheduled, uses "texts/presentation_scheduled.inc" as the main body.

`./presentation_send_badge_offer_email.py file.csv`

Send offer of human badge to presenter, uses "texts/presentation_human_badge.inc" as the main body. This script is special because it also creates a system to uniquely identify the presenter to help ensure a safe badge exchange with an unknown individual. Running this script makes a unique ID, using the first name of the presenter, with a 6 digit number appended to it. This ID is sent in the email, and also appended to a file called "presenter_badge_uniqIDs" with their full name and the ID. The presenter brings this information to the meeting and the identity of the presenter can be reasonably validated.
