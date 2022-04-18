#!/usr/bin/python3 
from rich import print
import os 
from simple_term_menu import TerminalMenu
import sys
import keyboard
from rst.autocomplete import SimpleCompleter, input_loop
from rst.lang_handler import lang_handler
from rst.ngrok_handler import ngrok_tunnel_creator, end_ngrok_connection, validate_tunnel_active
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

def listener_creator(listeners):
	lang,listener = listener_menu(listeners)
	rs = lang_handler(lang)
	print(rs) 
	
def take_choices(listeners,choice=""):
	history = []
	try:
		while True:
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
					listener_creator(listeners)
				except (KeyboardInterrupt,EOFError) as e:
					exit_script()
			else:
				help_menu(listeners)

			choice = ""
			history.append(choice)
	
	except KeyboardInterrupt:
		exit_script()
	except EOFError:
		exit_script()
	except Exception as e:
		print(f"[red]Script has errored out with error: {e}[red]")
		exit_script()

def main():
	#Checking for listeners
	listeners = listeners_check()
	
	#ASCII Art
	print("""
		██████╗░░██████╗████████╗
		██╔══██╗██╔════╝╚══██╔══╝
		██████╔╝╚█████╗░░░░██║░░░
		██╔══██╗░╚═══██╗░░░██║░░░
		██║░░██║██████╔╝░░░██║░░░
		╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░
	""")

	#Seeing is sys args are there 
	try:
		if sys.argv[1]:
			if "listen" in sys.argv[1]: 
				listener_creator(listeners)
	except:
		#If sys args are absent it throws an error so....
		take_choices(listeners)

if __name__=="__main__":
	main()
