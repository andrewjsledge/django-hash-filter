from django import template
from django.template.defaultfilters import stringfilter
from django.template.base import TemplateSyntaxError
import hashlib
from django_hash_filter.templatetags import get_available_hashes

register = template.Library()

@register.filter
@stringfilter
def hash(value, arg):
    """
    Returns a hex-digest of the passed in value for the hash algorithm given.
    """
    arg = str(arg).lower()
    if not arg in get_available_hashes():
        raise TemplateSyntaxError("The %s hash algorithm does not exist." % arg)
    try:
        f = getattr(hashlib, arg)
        hashed = f(value).hexdigest()
    except Exception:
        raise ValueError("The %s hash algorithm cannot produce a hex digest. Ensure that OpenSSL is properly installed." % arg)
    return hashed