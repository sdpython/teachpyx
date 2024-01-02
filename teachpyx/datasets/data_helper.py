import os


def get_data_folder():
    """
    Return the folder including data in this package.
    """
    this = os.path.dirname(__file__)
    data = os.path.join(this, "data")
    return os.path.abspath(data)
