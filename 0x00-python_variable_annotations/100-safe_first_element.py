#!/usr/bin/env python3

"""
module block docs
"""


from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augment the following code with the correct duck-typed annotations:

    # The types of the elements of the input are not know
        def safe_first_element(lst):
            if lst:
               return lst[0]
           else:
               return None
    """

    if lst:
        return lst[0]
    else:
        return None
