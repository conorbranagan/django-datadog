import os
import sys
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

reqs = []
if [sys.version_info[0], sys.version_info[1]] < [2, 7]:
    reqs.append("simplejson>=2.0.9")

setup(
    name = 'django-datadog',
    version = '0.1.0',
    packages = [
        'datadog',
        'datadog.middleware'
    ],
    include_package_data = True,
    license = 'BSD',
    description = ' simple Django middleware for submitting timings and exceptions to Datadog.',
    long_description = README,
    author = 'Conor Branagan',
    author_email = 'conor.branagan@gmail.com',
    install_requires = reqs.extend([
        'dogapi==1.2.1'
    ])
)