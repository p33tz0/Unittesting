import os

#Function that reads the filepath of this file and returns the filepath
def filepathread():
    filepath = os.path.dirname(os.path.realpath(__file__))
    return filepath
