#!/usr/bin/python3

def validUTF8(data):
    # Count the number of leading 1s in the most significant byte of each character
    num_bytes = 0
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
            else:
                if not (byte >> 6) == 0b10:
                    return False

        num_bytes -= 1

    return num_bytes == 0
