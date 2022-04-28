# RST | Reverse Shell Tool

![GitHub](https://img.shields.io/github/license/mustansirgodhrawala/rst)
![code size](https://img.shields.io/github/languages/code-size/mustansirgodhrawala/rst)
[![Documentation Status](https://readthedocs.org/projects/reverse-shell-tool/badge/?version=latest)](https://reverse-shell-tool.readthedocs.io/en/latest/?badge=latest)
![GitHub Build Status](https://img.shields.io/github/workflow/status/mustansirgodhrawala/rst/Tests)
![Code Coverage](https://codecov.io/gh/mustansirgodhrawala/rst/branch/master/graph/badge.svg?token=28PKVCT5G0)

## Description

Reverse Shell Tool by Mustansir Godhrawala. I created this tool to make the reverse shell process easier, rather than having to open pentest monkey's reverse shell cheatsheet and editing out the IP and PORT, the script will choose a random port and grab your IP and put it into your clipboard.

Heck we're even giving you options for listeners, you can use netcat or pwncat by Caleb Stewart and John Hammond for better post exploitation.

We'll create the payload and put it in your clipboard, and start the listener on our own too. All so you can spend your time pentesting rather than having to type quad 4 or 1234 again and again.

### **Run as sudo only.**

## Why use RST?

**Dude** making reverse shells is easy as  f\*\*k I mean I could go wherever I want copy the reverse shell..... aaahahahaha

Don't you see you have to go somewhere and copy shit and check the ip and what if you aren't pentesting with a vpn aaaaaaaaah

Let's take a look at a few scenarios and exactly how powerful reverse-shell-tool is....

1. Install rst on my linux box?
```bash
pip3 install reverse-shell-tool
```

2. Verify installation.
```bash
rst -v
```

### Scenarios:

1. Python reverse shell with pwncat listener using vpn ip?
```
rst -i v --lang py -l pwn
```
Breakdown:
- '-i' Specifies vpn ip
- '--lang' Specifies the language as py for valid shortforms see full documentation.
- '-l' Specifies the listener as pwncat


2. Netcat reverse shell for an openbsd box with netcat listener using local ip?
```
rst -i l --lang nc
```
Breakdown:
- '-i' Specifies the local ip, valid shortforms as l,v,n for local, vpn and ngrok respectively.
- '--lang' Specifies the language as netcat, for valid shortforms see full documentation.
- '-l' Specifies the default as netcat so need to specify.


3. Wanna do use case no 2 but have no vpn or local ip use? Use ngrok with the pyngrok library automate it with rst.
```
rst -i n --lang nc -n
```
Breakdown:
- '-i' Specifies the ngrok ip, valid shortforms as l,v,n for local, vpn and ngrok respectively.
- '--lang' Specifies the language as netcat, for valid shortforms see full documentation.
- '-l' Specifies the default as netcat so need to specify.
- '-n' Activates the ngrok library and does a one time installation of the binary.

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
