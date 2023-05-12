#!/usr/bin/python3
"""
Module that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    # create a set to keep track of opened boxes
    opened_boxes = set()

    # add the first box (index 0) to the set of opened boxes
    opened_boxes.add(0)

    # create a queue to keep track of boxes that have not yet been opened
    queue = boxes[0]

    while queue:
        # pop a box from the front of the queue
        box = queue.pop(0)

        # if the box has not already been opened
        if box not in opened_boxes:
            # add the box to the set of opened boxes
            opened_boxes.add(box)

            # add the keys in this box to the queue
            for key in boxes[box]:
                queue.append(key)

    # if the set of opened boxes contains all the boxes, return True
    if len(opened_boxes) == len(boxes):
        return True

    # otherwise, return False
    return False
