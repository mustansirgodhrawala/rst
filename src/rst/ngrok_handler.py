#!/usr/bin/python3
from pyngrok import ngrok, conf
import time
import subprocess

def ngrok_stat():
	process = subprocess.Popen(["which", "ngrok"], stdout=subprocess.PIPE)
	return process.communicate()[0]


def ngrok_tunnel_creator(local_port):
	process = subprocess.Popen(["which", "ngrok"], stdout=subprocess.PIPE)
	location = process.communicate()[0]
	# conf.get_default().ngrok_path = location.decode("utf-8")
	rs_tunnel = ngrok.connect(local_port, "tcp")
	public_ip, public_port = get_deets(rs_tunnel)
	return [public_ip,public_port]

def end_ngrok_connection():
	for tunnel in check_active_tunnels():
		ngrok.disconnect(tunnel.public_url)
		
def get_deets(tunnel):
	url = tunnel.public_url
	print(url)
	url_split = url.split(':',2)
	ip = url_split[0] + ":" + url_split[1]
	port = url_split[2]
	return [ip,port]

def check_active_tunnels():
	tunnels = ngrok.get_tunnels()
	return tunnels

def validate_tunnel_active():
	tunnels = check_active_tunnels()
	if tunnels:
		return True
	else:
		return False

