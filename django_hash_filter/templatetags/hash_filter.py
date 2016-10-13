import hashlib
import sys

from django import template
from django.template.defaultfilters import stringfilter
from django.template.base import TemplateSyntaxError
from django_hash_filter.templatetags import get_available_hashes

register = template.Library()

@register.filter
@stringfilter
def hash(value, arg):
    """
    Returns a hex-digest of the passed in value for the hash algorithm given.
    """
    arg = str(arg).lower()
    if sys.version_info >= (3,0):
        value = value.encode("utf-8")
    if not arg in get_available_hashes():
        raise TemplateSyntaxError("The %s hash algorithm does not exist. Supported algorithms are: %" % (arg, get_available_hashes()))
    try:
        f = getattr(hashlib, arg)
        hashed = f(value).hexdigest()
    except Exception:
        raise ValueError("The %s hash algorithm cannot produce a hex digest. Ensure that OpenSSL is properly installed." % arg)
    return hashed
