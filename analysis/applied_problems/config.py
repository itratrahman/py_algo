
def append_path(path):

    '''
    A function that adds  given directory to system path
    Arguments:
    path - directory which is to be appended to the system path
    '''

    # import the python system and os packages
    import sys
    import os

    # retrieve the absulute path of the directory
    path = os.path.abspath(path)
    # if the given path is not included in the system path
    # then add the path to python system path
    if path not in sys.path:
        sys.path.append(path)
