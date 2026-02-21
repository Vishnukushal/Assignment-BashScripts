#!/bin/bash

# Simple Log Analyzer Script

echo "-----------------------------"
echo "Log File Analyzer"
echo "-----------------------------"

# user log file path
echo "Enter the log file path:"
read logfile

# Check if file exists
if [ -f "$logfile" ]
then
    echo "File found. Analyzing..."

    echo "Total number of lines in log file:"
    wc -l "$logfile"

    echo "Number of ERROR entries:"
    grep -i "error" "$logfile" | wc -l

    echo "Number of WARNING entries:"
    grep -i "warning" "$logfile" | wc -l

    echo "Number of INFO entries:"
    grep -i "info" "$logfile" | wc -l

else
    echo "File does not exist. Please check the path."
fi