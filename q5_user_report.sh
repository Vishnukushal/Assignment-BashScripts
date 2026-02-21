#!/bin/bash

# User Account Report Scrip

echo "------------------------------------"
echo "User Account Security Report"
echo "------------------------------------"

# Total number of users in system
echo "Total number of users:"
cut -d: -f1 /etc/passwd | wc -l

echo "Users with UID 0 (Admin privileges):"
awk -F: '$3 == 0 {print $1}' /etc/passwd

echo "Currently logged-in users:"
who

echo "Users with Bash shell access:"
grep "/bin/bash" /etc/passwd | cut -d: -f1

echo "Report completed."
