# RST | Reverse Shell Tool

![GitHub](https://img.shields.io/github/license/mustansirgodhrawala/rst)
![code size](https://img.shields.io/github/languages/code-size/mustansirgodhrawala/rst)
[![Documentation Status](https://readthedocs.org/projects/reverse-shell-tool/badge/?version=latest)](https://reverse-shell-tool.readthedocs.io/en/latest/?badge=latest)
![GitHub Build Status](https://img.shields.io/github/workflow/status/mustansirgodhrawala/rst/Tests)
![Code Coverage](https://codecov.io/gh/mustansirgodhrawala/rst/branch/master/graph/badge.svg?token=28PKVCT5G0)](https://codecov.io/gh/mustansirgodhrawala/rst)
## Description

Reverse Shell Tool by Mustansir Godhrawala. I created this tool to make the reverse shell process easier, rather than having to open pentest monkey's reverse shell cheatsheet and editing out the IP and PORT, the script will choose a random port and grab your IP and put it into your clipboard.

Heck we're even giving you options for listeners, you can use netcat or pwncat by Caleb Stewart and John Hammond for better post exploitation.

We'll create the payload and put it in your clipboard, and start the listener on our own too. All so you can spend your time pentesting rather than having to type quad 4 or 1234 again and again.

### **Run as sudo only.**

## Installation Guide

### PYPI Install

1. Run pip install,  this will install all dependencies and build the wheel for you.
```bash
pip3 install reverse-shell-tool
```

### Source install

1. Clone the repo.
```bash
git clone https://github.com/mustansirgodhrawala/rst.git
```

2. Change directory into repo
```bash
cd rst
```

3. Run setup.py install
```bash
python3 setup.py install
```

**(Running rst in a python virtual env is recommended)**

### Documentation
For in-depth documentation on how the tool works and advanced usage you can find information at [Documentation](https://reverse-shell-tool.readthedocs.io/en/latest/).

**This project is under active development.**
