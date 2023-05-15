#!/usr/bin/python3

"""
Script that reads a log file line by line and computes metrics
"""

import sys
import re

# Define regular expression pattern to match log entries
LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'

# Create dictionary to store status code counts
STATUS_CODES =
{'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
 '500': 0}

# Initialize total size counter
TOTAL_SIZE = 0

# Open log file and read each line
with open('access.log') as log_file:
    for line in log_file:
        # Match log entry to pattern
        match = re.match(LOG_PATTERN, line)
        if match:
            # Extract status code and request size from log entry
            status_code = match.group(4)
            size = int(match.group(5))

            # Increment status code count and total size
            if status_code in STATUS_CODES:
                STATUS_CODES[status_code] += 1
            TOTAL_SIZE += size

            # Print status code counts every 10 entries
            if len(STATUS_CODES) % 10 == 0:
                print("Status code counts:", STATUS_CODES)

# Print final status code counts and total size
print("Status code counts:", STATUS_CODES)
print("Total size:", TOTAL_SIZE)
