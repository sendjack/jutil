"""
    Environmental Variables Utility
    -------------------------------

    A utility module for interacting with environmental variables.

"""
import os

from base_type import to_unicode, to_integer, UnicodeError
from decorators import constant


def _get_environmental_variable(key):
    """Look up an environmental variable by key and return str."""
    # all keys should be unicode
    if type(key) is not unicode:
        raise UnicodeError()

    byte_string = os.environ.get(str(key))

    if byte_string is None:
        print 'The key', key, 'is not in environment.'
        raise KeyError()

    return byte_string


def get_unicode(key):
    """Look up a environmental variable by key and return a unicode string by
    decoding the byte string to unicode with utf8."""
    return to_unicode(_get_environmental_variable(key))


def get_integer(key, default=None):
    """Look up an environmental variable by key and return an int."""
    byte_string = default

    try:
        byte_string = _get_environmental_variable(key)
    except KeyError as k:
        if default is None:
            raise k

    return to_integer(byte_string)


class _Environment(object):

    @constant
    def DEPLOYMENT(self):
        return "DEPLOYMENT"

    @constant
    def DEV(self):
        return "development"

    @constant
    def STAGING(self):
        return "staging"

    @constant
    def PROD(self):
        return "production"

ENV = _Environment()


class Deployment(object):

    @staticmethod
    def _is_deployment(value):
        return get_unicode(ENV.DEPLOYMENT) == value


    @staticmethod
    def is_solo():
        return not any([
                Deployment.is_dev(),
                Deployment.is_staging(),
                Deployment.is_prod(),
                ])


    @staticmethod
    def is_dev():
        return Deployment._is_deployment(ENV.DEV)


    @staticmethod
    def is_staging():
        return Deployment._is_deployment(ENV.STAGING)


    @staticmethod
    def is_prod():
        return Deployment._is_deployment(ENV.PROD)
