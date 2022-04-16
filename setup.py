import os
import re
from codecs import open

from setuptools import find_packages, setup

# Based on https://github.com/pypa/sampleproject/blob/main/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
long_description_content_type = "text/markdown"

setup(
    name="rst",
    version=VERSION,
    description="An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url="https://mustansirg.in/projects/rst",
    author="Mustansir Godhrawala",
    author_email="me@mustansirg.in",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
    # https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires
    # It is not considered best practice to use install_requires to pin dependencies to specific versions.
    install_requires=[
      rich==12.2.0
      setuptools==52.0.0
      simple_term_menu==1.4.1
      varname==0.8.3  
    ],
)
