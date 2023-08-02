# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.

"""
import sys
import traceback


def call_stack():
    """
    @return     traceback
    """
    exc_traceback = sys.exc_info()[-1]
    return traceback.extract_tb(exc_traceback), "".join(
        traceback.format_tb(exc_traceback)
    )
