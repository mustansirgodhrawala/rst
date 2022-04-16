#!/usr/bin/python3 
from rich import print
import os 
from varname import nameof
from simple_term_menu import TerminalMenu
import sys

languages = {
	'python':['python','py','py3'],
	'netcat':['nc','netcat'],
	'bash':['sh','bash'],
	'php':['php'],
	'ruby':['ruby'],
}

listeners = {
	'pwncat':['pwn','pwncat','pwncat-cs'],
	'netcat':['nc','netcat'],
	'socat':['socat','scat'],
}

def clear_console():
	print("\033c",end="")

def exit_script():
	print("\n[white]Thanks for using my tool[/white]")
	print("[white]Exiting[/white]")
	exit()

def help_menu():
	print("We provide the following options for languages and they can be paired with all listeners.")

	for dictionary in [languages,listeners]: 
		if dictionary == languages: 
			print("Languages")
		else:
			print("Listeners")
		for i in enumerate(dictionary):
			print(f"{i[0]}.{i[1].capitalize()}    ", end='')
		print('\n')

	print("The syntax to create listeners is as such: [language] [listener]")

def listener_menu():
	options_lang = [i for i in languages]
	terminal_menu_lang = TerminalMenu(options_lang, title="Languages")
	menu_entry_index_lang = terminal_menu_lang.show()
	lang = str(options_lang[menu_entry_index_lang])

	options_listener = [i for i in listeners]
	terminal_menu_listener = TerminalMenu(options_listener, title="Listeners")
	menu_entry_index_listener = terminal_menu_listener.show()
	listener = str(options_listener[menu_entry_index_listener])
	
def take_choices():
	try:
		while True:
			choice = input(">>>")
			if choice == "exit":
				exit_script()
			elif choice == "help":
				help_menu()
			elif choice == "clear":
				clear_console()
			elif choice == "listener":
				listener_menu()
			else:
				help_menu()

	except KeyboardInterrupt:
		exit_script()
	except EOFError:
		exit_script()
	except Exception as e:
		print(f"[red]Script has errored out with error: {e}[red]")
		exit_script()

def main():
	print("[white]Reverse Shell Tool[/white]")
	if 'listen' in str(sys.argv[1]):
		listener_menu()
	else:
		take_choices()

if __name__ == "__main__":
	main()