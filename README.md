# RST | Reverse Shell Tool 

## Description 

Reverse Shell Tool by Mustansir Godhrawala. I created this tool to make the reverse shell process easier, rather than having to open pentest monkey's reverse shell cheatsheet and editing out the IP and PORT, the script will choose a random port and grab your IP and put it into your clipboard. 

Heck we're even giving you options for listeners, you can use netcat or pwncat by Caleb Stewart and John Hammond for better post exploitation. 

We'll create the payload and put it in your clipboard, and start the listener on our own too. All so you can spend your time pentesting rather than having to type quad 4 or 1234 again and again. 

### **Run as sudo only.** 

## Installation Guide

In depth guide:
1. View the setup script in the browser and click on it. 
2. Click on the view raw file, and copy the link from the browser search bar. 
3. Wget the setup script. Using the below command. 
```bash
wget https://raw.githubusercontent.com/mustansirgodhrawala/rst/master/setup
```
4.Run the following command
```bash
chmod +x setup
```

5. Execute the command using the below command
```bash 
./setup
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
1. rst python [Python payload with default netcat listener]
2. rst ruby [Ruby Payload with default netcat listener]
3. rst nc 2 [2 For pwncat listener]
4. rst python pwncat [Python payload with pwncat listener]
5. rst ruby nc [Ruby payload with netcat listener]
```
