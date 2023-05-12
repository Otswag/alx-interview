Log Parsing Script
This script reads stdin line by line and computes metrics based on the input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints the following statistics from the beginning:

Total file size: <total size>
Number of lines by status code:
<status code>: <number>
Possible status codes are: 200, 301, 400, 401, 403, 404, 405, and 500.

Author
This script was written by Emmanuel C. Amadi