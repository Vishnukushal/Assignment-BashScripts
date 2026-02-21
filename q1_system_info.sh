#!/bin/bash

# This script displays basic system information

echo "System Information"
echo "--------------------------"

# It display host name
echo "Hostname:"
hostname

# It shows Current user
echo "Current User:"
whoami

# It shows Date
echo "Date :"
date

#this shows uptime of System
echo "System Uptime:"
uptime

# This shows current Version of Kernel
echo "Kernel Version:"
uname -r

# This shows Memory Usage
echo "Memory Usage:"
free -h

# This shows Disk usage
echo "Disk Usage:"
df -h
