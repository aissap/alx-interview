#!/usr/bin/python3

import sys
import signal
"""Log parsing"""

total_file_size = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}
line_count = 0


def print_stats():
    """
    Print accumulated metrics.
    Outputs:
        - Total file size processed so far
        - Count of each status code in ascending order of status codes
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C).
    Args:
        sig: Signal number
        frame: Current stack frame
    Action:
        Prints the current statistics and exits the program
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except ValueError:
            continue

        total_file_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

except Exception as e:

    sys.stderr.write("Error: {}\n".format(e))
finally:

    print_stats()
