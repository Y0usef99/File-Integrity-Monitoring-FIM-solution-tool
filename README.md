# File-Integrity-Monitoring-FIM-solution-tool-using python script

The tool has two modes:
• Normal Mode:
o Start to audit any changes that happen in a specific directory
every 60 seconds.
o If there is a file deleted, modified, or added, report it into
the Console and write them into a log file (send mail is a bonus)
o Every change will be logged with its date as a key [dictionary]
• Aggressive mode
o Create a mirror of the user-given directory hierarchy.
o In your mirror copy, folders’ names will have the same as the
original, but files will be renamed by the content md5 of the
original file data.
o Changes will be logged every 60 seconds.
o What if the file has been modified?
▪ Create a new copy (with the same technique) and report
the event as mentioned in the normal mode.
o Same in deletion or creation. 
