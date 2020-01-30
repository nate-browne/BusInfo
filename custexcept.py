#!/usr/bin/env python3


class APIException(Exception):
    '''
    Custom exception for errors that arise as a result of the API
    being used.\n
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize an exception of this type
        '''
        Exception.__init__(self, *args, **kwargs)


class APIInitException(APIException):
    '''
    Custom exception for errors that arise in the constructor for the
    custom class that uses the API.\n
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize an exception of this type
        '''
        APIException.__init__(self, *args, **kwargs)
