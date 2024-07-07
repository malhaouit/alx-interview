#!/usr/bin/python3
"""This module provides a function to determine if all locked boxescan be
opened.
Each box may contain keys to other boxes. The first box is always unlocked.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened starting from the first box.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist represents
                                 a box containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Examples:
        >>> canUnlockAll([[1], [2], [3], [4], []])
        True
        >>> canUnlockAll([
            [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]
            ])
        True
        >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
        False
    """
    all_keys = set()
    opened_boxes = set()
    opened_boxes.add(0)
    all_keys.update(boxes[0])

    while len(all_keys) != 0:
        new_keys = all_keys.copy()
        all_keys.clear()

        for key in new_keys:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                all_keys.update(boxes[key])

    if len(opened_boxes) == len(boxes):
        return True

    return False
