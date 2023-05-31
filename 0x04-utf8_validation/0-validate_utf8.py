#!/usr/bin/python3

def validUTF8(data):
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                remaining_bytes += 1
                mask >>= 1

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

            if remaining_bytes > 0:
                remaining_bytes -= 1
            else:
                if (byte >> 6) != 0b10:
                    return False

            remaining_bytes -= 1

            if remaining_bytes < 0:
                return False

    return remaining_bytes == 0
