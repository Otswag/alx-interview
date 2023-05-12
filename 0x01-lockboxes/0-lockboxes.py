#!/usr/bin/python3
"""
Module that contains a function that determines if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Args:
        boxes (list): A list of lists containing the keys.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked_boxes = [False] * n
    unlocked_boxes[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])
    return all(unlocked_boxes)
