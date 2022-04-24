#!/usr/bin/python3 
from rich import print
import os 
from simple_term_menu import TerminalMenu
import sys
import keyboard
from rst.autocomplete import SimpleCompleter, input_loop
from rst.lang_handler import lang_handler, provide_rs
from rst.ngrok_handler import ngrok_tunnel_creator, end_ngrok_connection, validate_tunnel_active,ngrok_stat
import argparse
from typing import Sequence, Optional
from rst.conn_handler import conn_handler
from rst.listener_handler import activate_listener
import subprocess
try:
    import gnureadline as readline
except ImportError:
    import readline


languages = {
	'python':['python','py','py3'],
	'netcat':['nc','netcat'],
	'bash':['sh','bash'],
	'php':['php'],
	'ruby':['ruby'],
}

def listeners_check():
	listeners = {}
	def netcat_check():
		if os.path.isfile("/usr/bin/nc"):
			listeners['netcat']=['nc','netcat']
	def socat_check():
		if os.path.isfile("/usr/bin/socat"):
			listeners['socat']=['socat','scat']
	def pwncat_check():
		#Checking for pwncat
		if os.path.isdir('/opt/pwncat'):
			listeners['pwncat']=['pwn','pwncat','pwncat-cs']

	netcat_check()
	socat_check()
	pwncat_check()

	return listeners

def clear_console():
	print("\033c",end="")

def exit_script():
	print("\n[white]Thanks for using my tool[/white]")
	print("[white]Exiting[/white]")
	exit()

def help_menu(listeners):
	print("We provide the following options for languages and they can be paired with all listeners.")

	for dictionary in [languages,listeners]: 
		if dictionary == languages: 
			print("Languages")
		else:
			print("Listeners")
		for i in enumerate(dictionary):
			print(f"{i[0]}.{i[1].capitalize()}    ", end='')
		print('\n')

	print("The syntax to create listeners is as such: <language> <listener>")
	print("Or you can enter the listen to get a gui based menu.")
	if ngrok_stat():
		print("Use -n when launching to use ngrok in reverse shell, we'll do the ngroking for you.")
	else:
		print("#### Support for ngrok is disabled since it is not installed locally.")

def listener_menu(listeners):
	options_lang = [i for i in languages]
	terminal_menu_lang = TerminalMenu(options_lang, title="Languages")
	menu_entry_index_lang = terminal_menu_lang.show()
	lang = str(options_lang[menu_entry_index_lang])

	options_listener = [i for i in listeners]
	terminal_menu_listener = TerminalMenu(options_listener, title="Listeners")
	menu_entry_index_listener = terminal_menu_listener.show()
	listener = str(options_listener[menu_entry_index_listener])
	
	return [lang,listener]

def listener_creator(listeners, ngrok_use,option=False, lang="",listener="",ip_spec=""): 
	if not lang and not listener:
		lang,listener = listener_menu(listeners)
	rs = lang_handler(lang, optdion)
	data = conn_handler(ngrok_use, ip_spec)
	
	local_port = ""

	try:
		ip,port,local_port = data
	except:
		ip,port = data

	provide_rs(rs,ip,port)

	if not local_port:
		activate_listener(listeners, listener, port,ngrok_use)
	else:
		activate_listener(listeners, listener, local_port,ngrok_use)


def take_choices(listeners,ngrok_use,choice=""):
	history = []
	while True:
		try:
			if not choice:
				OPTIONS = ['help', 'clear', 'listen', 'exit']
				readline.set_completer(SimpleCompleter(OPTIONS).complete)
				# Use the tab key for completion
				readline.parse_and_bind('tab: complete')
				# Prompt the user for text
				choice = input_loop()

			if choice == "exit":
				exit_script()

			elif choice == "help":
				help_menu(listeners)
				
			elif choice == "clear":
				clear_console()
			elif "listen" in choice:
				try:
					listener_creator(listeners,ngrok_use)
				except (KeyboardInterrupt,EOFError) as e:
					exit_script()
			else:
				help_menu(listeners)

			choice = ""
			history.append(choice)

		except KeyboardInterrupt:
			print("Enter exit or hit Ctrl+d to exit.")
		except EOFError:
			exit_script()
		except Exception as e:
			print(f"[red]Script has errored out with error: {e}[red]")
			exit_script()

def main(argv: Optional[Sequence[str]] = None):
	#ASCII Art
	print("""
		██████╗░░██████╗████████╗
		██╔══██╗██╔════╝╚══██╔══╝
		██████╔╝╚█████╗░░░░██║░░░
		██╔══██╗░╚═══██╗░░░██║░░░
		██║░░██║██████╔╝░░░██║░░░
		╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░
	
						By Mustansir Godhrawala
						ver: 1.0
	""")

	#Checking for listeners
	listeners = listeners_check()
	ngrok_use = False

	# Argument Parsing
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', help="Run with a -n flag to use ngrok when making reverse shell.",action="store_true")
	parser.add_argument('-m', help="Run with a -m flag to open with the listener menu.",action="store_true")
	parser.add_argument('--lang', type=str, help="Use the --lang flag to specify the language for the listener.")
	parser.add_argument('-l','--listener', type=str, help="Use the -l flag to specify the listener. Default=netcat",default="netcat")
	parser.add_argument('-i','--ip', type=str, help="Set the -i flag to v for 'vpn' ip, 'l' for local ip and 'n' for ngrok.",default="")
	parser.add_argument('-b','--basic', action='store_true', help="Set the -b flag to use the most basic reverse shell there is.")

	#Processing args
	args = parser.parse_args(argv)
	#Shortening the ip choice
	if len(args.ip) > 1:
		args.ip = args.ip[0]
	if args.n:
		if ngrok_stat():
			print("Ngrok will be used in reverse shell creation.")
			ngrok_use = True
		else:
			print("Ngrok is not installed, exiting program.")
			print("Please install ngrok at \"https://ngrok.com/download\"")
			exit()
	if args.m:
		listener_creator(listeners, ngrok_use,args.ip)
	if args.lang:
		listener_creator(listeners, ngrok_use,args.basic, args.lang, args.listener,args.ip)


	take_choices(listeners, ngrok_use)

if __name__=="__main__":
	main()
