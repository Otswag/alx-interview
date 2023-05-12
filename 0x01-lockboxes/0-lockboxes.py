#!/usr/bin/python3
"""
Module that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes: A list of lists containing the keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    # Create a set to keep track of all the boxes that have been opened.
    opened_boxes = set()
    # Add the first box (index 0) to the set of opened boxes.
    opened_boxes.add(0)
    # Create a queue to keep track of boxes that have not yet been opened.
    unopened_boxes = boxes[0][:]
    # While there are still unopened boxes:
    while unopened_boxes:
        # Pop a box from the front of the queue.
        box = unopened_boxes.pop(0)
        # If we have not already opened this box:
        if box not in opened_boxes:
            # Add it to the set of opened boxes.
            opened_boxes.add(box)
            # Add all the keys in this box to the queue of unopened boxes.
            unopened_boxes.extend(boxes[box])
    # If the set of opened boxes contains all the boxes, return True.
    if len(opened_boxes) == len(boxes):
        return True
    # Otherwise, return False.
    return False
