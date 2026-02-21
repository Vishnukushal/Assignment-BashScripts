#!/bin/bash

# Simple File Manager Script

while true
do
    echo "-----------------------------"
    echo "Simple File Manager"
    echo "1. Create a File"
    echo "2. Delete a File"
    echo "3. Create a Directory"
    echo "4. List Files in Current Directory"
    echo "5. Exit"
    echo "-----------------------------"

    echo "Enter your choice:"
    read choice

    if [ "$choice" -eq 1 ]
    then
        echo "Enter file name to create:"
        read filename
        touch "$filename"
        echo "File created successfully."

    elif [ "$choice" -eq 2 ]
    then
        echo "Enter file name to delete:"
        read filename
        rm -i "$filename"
        echo "Delete operation completed."

    elif [ "$choice" -eq 3 ]
    then
        echo "Enter directory name to create:"
        read dirname
        mkdir "$dirname"
        echo "Directory created successfully."

    elif [ "$choice" -eq 4 ]
    then
        echo "Files in current directory:"
        ls

    elif [ "$choice" -eq 5 ]
    then
        echo "Exiting program..."
        break

    else
        echo "Invalid choice. Please try again."
    fi

done