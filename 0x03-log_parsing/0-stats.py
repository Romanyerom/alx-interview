#!/usr/bin/python3
import sys

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Parse the relevant parts of the log line
            ip = parts[0]
            date = parts[3] + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code count if valid
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Every 10 lines, print the statistics
            if line_count % 10 == 0:
                print_stats()

        except Exception:
            # Skip lines that don't match the expected format
            continue

except KeyboardInterrupt:
    # On keyboard interruption, print final stats
    print_stats()
    raise

# In case the input stops before an interrupt and not a multiple of 10
print_stats()

