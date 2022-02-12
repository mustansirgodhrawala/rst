# RST | Reverse Shell Tool 

## Description 

Reverse Shell Tool by Mustansir Godhrawala. I created this tool to make the reverse shell process easier, rather than having to open pentest monkey's reverse shell cheatsheet and editing out the IP and PORT, the script will choose a random port and grab your IP and put it into your clipboard. 

Heck we're even giving you options for listeners, you can use netcat or pwncat by Caleb Stewart and John Hammond for better post exploitation. 

We'll create the payload and put it in your clipboard, and start the listener on our own too. All so you can spend your time pentesting rather than having to type quad 4 or 1234 again and again. 

## Installation Guide

In depth guide:
1. View the script in the browser and click on it. 
2. Click on the view raw file, and copy the link from the browser search bar. 
3. Wget the setup script. Using the below command. 
```bash
wget <copy_paste_link_here>
```
4.Run the following command
```bash
chmod +x setup
```

5. Execute the command using the below command
```bash 
setup
```

OR

1. Clone the repo.
```bash
git clone https://github.com/mustansirgodhrawala/rst.git
```
2. Change the directory.
```bash
cd rst 
```
3.  Give setup execution permissions.
```bash
chmod +x setup
```
4. Run the setup shell script. 
```bash
./setup
```

All done, the 'rst' script is ready to use. 
## Usage

```bash
1. rst python
2. rst ruby
3. rst nc 2 [2 For pwncat listener]
```

## Requirements 
1. This is a barebones bash script that needs netcat on your system and pwncat if you plan on using it.

## To-Do
1. Manage colour schemes. 
2. Add socat as a listener. 
3. Try to auto-stabilize netcat and socat reverse shells. 
4. Give php full rev shells options. 
