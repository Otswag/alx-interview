#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else False
    """
    if not boxes:
        return False

    # Create a set of the box indices, and mark box 0 as opened
    box_indices = set(range(len(boxes)))
    opened_boxes = {0}

    # Iterate through the list of boxes
    while box_indices:
        # Get the set of keys in the opened boxes
        keys = set(key for box in opened_boxes for key in boxes[box])

        # Find the set of boxes that can be opened with the keys
        openable_boxes = box_indices.intersection(keys)

        # If there are no more openable boxes, break out of the loop
        if not openable_boxes:
            break

        # Mark the openable boxes as opened, and remove them from the set of unopened boxes
        opened_boxes.update(openable_boxes)
        box_indices.difference_update(openable_boxes)

    # Return True if all boxes have been opened, else False
    return not box_indices
