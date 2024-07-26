#!/usr/bin/python3
"""This module covers UTF-8 validation task."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list of int): The data set represented by a list of integers, where
    each integer represents 1 byte.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    def is_continuation_byte(byte):
        """
        Checks if a byte is a valid UTF-8 continuation byte (10xxxxxx).

        Args:
        byte (int): The byte to check.

        Returns:
        bool: True if the byte is a continuation byte, else False.
        """
        return (byte & 0b11000000) == 0b10000000

    n_bytes = 0

    for byte in data:
        if n_bytes == 0:
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                n_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                n_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                n_bytes = 3
            else:
                return False
        else:
            if not is_continuation_byte(byte):
                return False
            n_bytes -= 1

    return n_bytes == 0
