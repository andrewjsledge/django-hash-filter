import sys
import hashlib

if sys.version_info < (2, 5):
    raise ImportError("django-hash-filter requires Python 2.5+")


def get_available_hashes():
    """
    Returns a tuple of the available hashes
    """
    if sys.version_info >= (3,2):
        return hashlib.algorithms_available
    elif sys.version_info >= (2,7) and sys.version_info < (3,0):
        return hashlib.algorithms
    else:
        return 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
