# RST | Reverse Shell Tool 

## Description 

Reverse Shell Tool by Mustansir Godhrawala. I created this tool to make the reverse shell process easier, rather than having to open pentest monkey's reverse shell cheatsheet and editing out the IP and PORT, the script will choose a random port and grab your IP and put it into your clipboard. 

Heck we're even giving you options for listeners, you can use netcat or pwncat by Caleb Stewart and John Hammond for better post exploitation. 

We'll create the payload and put it in your clipboard, and start the listener on our own too. All so you can spend your time pentesting rather than having to type quad 4 or 1234 again and again. 

## Installation 

```bash
./setup.sh
```
## Usage

```bash
rst help
```

### Requirements 
1. This is a barebones bash script that needs netcat on your system and pwncat if you plan on using it. We don't have checks for pwncat installation yet so please make sure it's there. 

## To-Do
1. Manage colour schemes. 
2. Setup pwncat checks. 
3. Add more language for reverse shell payloads. 
4. Add socat as a listener. 
5. Try to auto-stabilize netcat and socat reverse shells. 
6. Give php full rev shells options. 