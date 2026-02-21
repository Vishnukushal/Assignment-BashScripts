#!/bin/bash

# Simple Backup Script

echo "-----------------------------"
echo "Simple Backup Script"
echo "-----------------------------"

# user directory to backup
echo "Enter the full path of directory to backup:"
read dirpath

# Check if directory exists
if [ -d "$dirpath" ]
then
    echo "Directory found. Creating backup..."

    # Get current date and time
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

    # Create backup file name
    backupname="backup_$timestamp.tar.gz"

    # Create compressed backup
    tar -czf "$backupname" "$dirpath"

    echo "Backup created successfully!"
    echo "Backup file name: $backupname"

else
    echo "Directory does not exist. Please check the path."
fi