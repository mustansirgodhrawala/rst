import ipaddress
import random
import socket

import netifaces
from simple_term_menu import TerminalMenu

from rst.ngrok_handler import (
    ngrok_tunnel_creator,
)
from rst.rst import exit_script


def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def vpn_ip_check():
    try:
        addrs = netifaces.ifaddresses("tun0")
        ip = addrs[netifaces.AF_INET][0]["addr"]
        return ip
    except Exception:
        return False


def local_ip_check():
    ips = []
    netmasks = []
    try:
        # Assessing and collecting all options for ip addresses
        for interface in netifaces.interfaces():
            if "en" in interface or "wlp" in interface or "wlan" in interface:
                addrs = netifaces.ifaddresses(interface)
                try:
                    ips.append(addrs[netifaces.AF_INET][0]["addr"])
                    netmasks.append(addrs[netifaces.AF_INET][0]["netmask"])
                except Exception:
                    pass

        # Checking which ip is the local ip
        for i in range(0, len(ips)):
            net = ipaddress.ip_network(f"{ips[i]}/{netmasks[i]}", strict=False)
            if str(net).split("/")[-1] == "24":
                if str(net).split(".")[0] != "10":
                    return ips[i]

    except Exception as e:
        print(e)


def random_port():
    while True:
        port = random.randint(3000, 65535)
        if is_port_in_use(port):
            continue
        else:
            return port


def conn_handler(ngrok_use, ip_spec=""):
    # IP Address Part
    options = []
    if vpn_ip_check():
        vpn_ip = vpn_ip_check()
        options.append("VPN IP")
    if local_ip_check():
        local_ip = local_ip_check()
        options.append("Local IP(Behind NAT)")
    if ngrok_use:
        options.append("Ngrok Public")

    if not ip_spec:

        terminal_menu_lang = TerminalMenu(options, title="Reverse IP")
        choice = terminal_menu_lang.show()

        if "VPN" in options[choice]:
            port = random_port()
            return [vpn_ip, port]
        elif "Local" in options[choice]:
            port = random_port()
            return [local_ip, port]
        elif "Ngrok" in options[choice]:
            port = random_port()
            ngrok_ip, ngrok_port = ngrok_tunnel_creator(port)
            return [ngrok_ip, ngrok_port, port]

    else:
        if ip_spec == "l":
            if local_ip:
                return [local_ip, random_port()]
            else:
                local_ip = input("Couldn't grab local ip, please specify manually.")
                return [local_ip, random_port()]
        elif ip_spec == "v":
            if vpn_ip:
                return [vpn_ip, random_port()]
            else:
                vpn_ip = input("Couldn't find vpn ip, please enter manually.")
                return [vpn_ip, random_port()]
        elif ip_spec == "n":
            if ngrok_use:
                port = random_port()
                ngrok_ip, ngrok_port = ngrok_tunnel_creator(port)
                return [ngrok_ip, ngrok_port, port]
            else:
                print(
                    "To use ngrok please run with -n flag or enter ngrok=True from console."
                )
                exit_script()
