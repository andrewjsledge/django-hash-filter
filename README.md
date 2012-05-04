django-hash-filter
==================

Provides a simple filter to produce hashed (hex digest) values in templates.

Install
=======

```shell
$ pip install django-hash-filter
```

Usage
=====
```python
{% load hash_filter %}
{{ string_variable|hash:"sha256" }}
```