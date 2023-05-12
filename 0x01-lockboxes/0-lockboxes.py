#!/usr/bin/python3
"""Module that contains a function that determines if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Args:
        boxes (list): A list of lists containing the keys.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    keys = [0] + boxes[0]
    unlocked = set(keys)
    for key in keys:
        if key < n:
            for box in boxes[key]:
                if box not in unlocked:
                    unlocked.add(box)
                    keys.append(box)
    return len(unlocked) == n
