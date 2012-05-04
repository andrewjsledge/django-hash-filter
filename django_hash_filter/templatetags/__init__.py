import sys
import hashlib

if sys.version_info < (2, 5):
    raise ImportError("django-hash-filter requires Python 2.5+")


def get_available_hashes():
    """
    Returns a tuple of the available hashes
    """
    if sys.version_info >= (2,7):
        return hashlib.algorithms
    return 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
