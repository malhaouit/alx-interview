#!/usr/bin/python3
"""This module covers an example of log parsing"""

import sys
import re
from collections import defaultdict

total_file_size = 0
flag = 0
status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = defaultdict(int)

try:
    for line in sys.stdin:
        pattern = (
            r'(\d+\.\d+\.\d+\.\d+)'  # IP Address
            r' - '                    # Separator
            r'\[(.*?)\]'              # Date
            r' "GET /projects/260 HTTP/1\.1"'  # Request
            r' (\d+)'                 # Status code
            r' (\d+)'                 # File size
        )
        match = re.match(pattern, line)

        if match:
            ip, date, status_code, file_size = match.groups()

            total_file_size += int(file_size)
            if int(status_code) in status_code_list:
                status_code_counts[int(status_code)] += 1

            flag += 1

            if flag == 10:
                print("File size: {}".format(total_file_size))
                for code in sorted(status_code_counts):
                    print("{}: {}".format(code, status_code_counts[code]))
                flag = 0

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))
