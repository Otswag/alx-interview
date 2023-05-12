#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- Total file size: File size: <total size>
  where <total size> is the sum of all previous <file size>
- Number of lines by status code:
  possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  if a status code doesn’t appear or is not an integer, don’t print anything for this status code
  format: <status code>: <number>
  status codes should be printed in ascending order

Usage:
$ ./0-stats.py < access.log
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics for the given total size and status codes.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary that maps status codes to their counts.
    """
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{:d}: {:d}".format(status_code, status_codes[status_code]))


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    i = 0

    try:
        for line in sys.stdin:
            if i != 0 and i % 10 == 0:
                print_stats(total_size, status_codes)

            i += 1
            tokens = line.strip().split()
            if len(tokens) == 7:
                ip_address, _, _, timestamp, _, status_code, file_size = tokens
                if status_code.isdigit() and int(status_code) in status_codes:
                    status_codes[int(status_code)] += 1
                    total_size += int(file_size)
                else:
                continue
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == '__main__':
    main()
