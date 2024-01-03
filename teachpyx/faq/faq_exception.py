# coding: utf-8
import sys
import traceback


def call_stack():
    """
    :return: traceback
    """
    exc_traceback = sys.exc_info()[-1]
    return traceback.extract_tb(exc_traceback), "".join(
        traceback.format_tb(exc_traceback)
    )
