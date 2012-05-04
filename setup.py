from setuptools import setup, find_packages

setup(
    name='django-hash-filter',
    version='1.1',
    packages=find_packages(),
    url='https://github.com/andrewjsledge/django-hash-filter',
    license='MIT',
    author='Andrew Sledge',
    author_email='andrew.j.sledge@gmail.com',
    description='Provides a simple filter to produce hashed (hex digest) values in templates.',
    install_requires = ["django >= 1.3"],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
