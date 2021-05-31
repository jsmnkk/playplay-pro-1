import requests, sys, time, json, os, psutil, random, colorama, _thread
from colorama import Fore, Back, Style
from flask import *
from datetime import datetime
import config

os.system("clear")
os.environ['TZ'] = 'Asia/Jakarta'

jwt_token = config.jwt_token
userId = config.userId
trace_id = config.trace_id
user_agent = config.user_agent

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['BOT_STARTED'] = False
app.config['limited_game'] = 0
app.config['total_req'] = 0
app.config['status'] = 'OFFLINE'
app.config['ERR_MESS'] = "TIDAK ADA"
app.config['CAN_START'] = True

def verify(userId):
    h = {
        "Accept-Charset": "UTF-8",
        "trace_id": "d3485d5cc9e240ecb189165103d9b0b9",
        "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhSnNvbiI6IntcInVzZXJJZFwiOlwiNzM4NTA5NTI4MjU4Mzk2MTZcIixcIm5hbWVcIjpcIjExMzAwMTEzMzc1NDcxNjY1ODAzNV81XCIsXCJuaWNrbmFtZVwiOlwiSm9vb1wiLFwiYXZhdGFyVXJsXCI6XCJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDFBanoxd1lGNUU2bG5vak1mVTY0OU5zblpyMFhnaUxEcE5pMzdzUT1zOTYtY1wiLFwiY291bnRyeVwiOlwiSURcIixcInBsYXRmb3JtXCI6NSxcInNvdXJjZVwiOlwiMVwiLFwiY3JlYXRlVGltZVwiOjE2MjIxNTE5NTkwMDAsXCJ1cGRhdGVUaW1lXCI6MTYyMjE1MTk1OTAwMCxcInN0YXR1c1wiOjB9IiwiZXhwIjoxNjI0NzkxNTM3fQ.PNPT8PANRixVajkxiOqRKuXqouDk94VxdtcF3S5Q-H4",
        "portal": "api",
        "userId": "73850952825839616",
        "Accept-Encoding": "gzip,br",
        "Content-Type": "application/json",
        "Content-Length": "943",
        "Host": "api.funluck.net",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.12.1"
    }
    url = "http://api.funluck.net/activity/invite-bind/list?trace_id\u003dd3485d5cc9e240ecb189165103d9b0b9"
    body = {"s":"A4AAAAAuSo8qahpLgcTIWBp1SIprAXqzXtXXVxrZzLnkshxRu6lzWUUMYr53wjAP96W\/3kq5qyQYkc+\/61gt1152xQe3Pwt8FIphcF0vfiZoTGvs3abH6hRif4R+wt\/+mjQbNR9N4CFsDdoKYmXfnsn5O7SbTa1BxG\/1hlqMIIlQvqGF3PdhpkprUfqR608FoCY+wpgWy7e4vi6t1ru681H4K1jloKltq\/Azi0N0VByFcr\/1h7OB3oZcb70Xt7Ffcxi3lmPW2CCC83LZ\/Mn+NUGcXBFbR\/6E22ma1uQP9gFG0raTr5EXokFrwv1N4yCw9YWSY7Vc7HNDmonlmo1EOFdpkgnYHDh+2bzPjtszTuNK5oLW0GaY2eRjgTmonzjkwxGQy0VMearbrsGUwkPZndyCKflHHygO0sFfQmTG7HcTAsvrbX80Zf9xuZpp9+3EeZhBhH9E23NDx8VQlJ5b7846LyGFbq57NYhIgq7mwbVXbyg6nqcYZDocdpQmprdyqCIMqoeU00+murOarLTbqKwpYODpkDGPQnC0Prsy5yOepet9aGOpoVnniHii7FzVyGA0C19Oy0+T35m5xI8tVtSvWYNoegDvnvRVbi3+kKekc5OXkN0USjJhUlIJyd4M7395rrIqlg1pwQa8NKwhNCMmDriyCBv9Ro+cwcMlrg83XM6MFIgpaEmiBrChDla+LH\/v+xTPADfhp1kA93MOoBypWo8QFDV1na3rsupnUVP5qkTUZEDihFO9bwGAqPLpZji8Vxns8wtBrdh9R86Pi+awNXqKW0ITL1TgNcGRMHRnongIT5G\/Dd+GFmeDhEDOjFTCSCo29t1kWHyzXfHHmsjffvR1h0RokwPICFl3IBaLjFacy5VxbB2yCmnuIpLrqFbCzQ\/tcBhhx2DdvhAeZ+I7K3yx"}

    req = requests.post(url, headers=h, json=body).json()
    data = req['data']['dataLs']
    res = 0
    for i in data:
        if i['userId'] == userId:
            res +=1
    return res

def profile():
    url = config.profile_url
    h = {
        "jwt-token":jwt_token,
        "userId":userId,
        "trace_id": trace_id,
        "portal":"api",
        "Accept-Encoding":"gzip,br",
        "Host":"api.funluck.net",
        "Connection":"Keep-Alive",
        "User-Agent": "okhttp/3.12.1"
    }
    req = requests.get(url, headers=h).json()
    return req

def game1():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game1['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game1['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req

def game2():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game2['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game2['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req

def game3():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game3['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game3['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req


def game4():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game4['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game4['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req


def game5():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game5['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game5['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req


def game6():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game6['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game6['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req


def game7():
    h =  {
        "Host": "api.funluck.net",
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": config.jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game7['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q\u003d0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }

    url = "http://api.funluck.net/activity/h5-game/record-flow"

    body = config.game7['data']

    req = requests.post(url, headers=h, json=body).json()
    return req

def game8():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game8['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game8['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req

def game9():
    host = "api.funluck.net"
    header = {
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game9['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q=0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }
    json_data_game = config.game9['data']
    url_game = f'http://{host}/activity/h5-game/record-flow'
    req = requests.post(
        url=url_game, 
        headers=header,
        json=json_data_game
    ).json()

    return req

def game10():
    h = {
        "Host": "api.funluck.net",
        "Connection": "keep-alive",
        "Content-Length": "892",
        "jwt-token": config.jwt_token,
        "Origin": "http://game.funluck.net",
        "gUserId": userId,
        "User-Agent": user_agent,
        "userId": userId,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": config.game10['url'],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "id-ID,en-US;q\u003d0.9",
        "X-Requested-With": "com.funmaker.gamematrix"
    }

    body = config.game10['data']

    url = "http://api.funluck.net/activity/h5-game/record-flow"

    req = requests.post(url, headers=h, json=body).json()
    return req

colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
hijau2 = Style.BRIGHT+Fore.GREEN
putih = Style.RESET_ALL
abu2 = Style.DIM+Fore.WHITE
putih2 = Style.BRIGHT+Fore.WHITE
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
ungu2 = Style.BRIGHT+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
yellow2 = Style.BRIGHT+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
red2 = Style.BRIGHT+Fore.RED
biru = Style.BRIGHT+ Fore.BLUE
cyan =Style.BRIGHT+ Fore.CYAN
kur1 = "\033[1;31m"+"["
kur2 = "\033[1;31m"+"]"


def mine():
    num = 0
    limited_game = []
    limited = 0
    game = 0
    app.config['BOT_STARTED'] = True
    app.config['status'] = 'ONLINE'
    while limited < 10:
        app.config['limited_game'] = limited
        app.config['total_req'] = num
        if not "game1" in limited_game:
            time.sleep(3)
            data = game1()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 1")
                
            else:
                print("\r")
                print("LIMITED GAME 1!".format(ungu2, hijau2, ungu2, putih, hijau2))                
                limited_game.append("game1")
                limited += 1
        elif not "game2" in limited_game:
            time.sleep(3)
            data = game2()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 2")
                
            else:
                print("\r")
                print("LIMITED GAME 2!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game2")
                limited += 1
        elif not "game3" in limited_game:
            time.sleep(3)
            data = game3()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 3")
                
            else:
                print("\r")
                print("LIMITED GAME 3!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game3")
                limited += 1
        elif not "game4" in limited_game:
            time.sleep(3)
            data = game4()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 4")
                
            else:
                print("\r")
                print("LIMITED GAME 4!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game4")
                limited += 1
        elif not "game5" in limited_game:
            time.sleep(3)
            data = game5()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 5")
                
            else:
                print("\r")
                print("LIMITED GAME 5!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game5")
                limited += 1
        elif not "game6" in limited_game:
            time.sleep(3)
            data = game6()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 6")
                
            else:
                print("\r")
                print("LIMITED GAME 6!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game6")
                limited += 1
        elif not "game7" in limited_game:
            time.sleep(3)
            data = game7()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 7")
                
            else:
                print("\r")
                print("LIMITED GAME 7!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game7")
                limited += 1
        elif not "game8" in limited_game:
            time.sleep(3)
            data = game8()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 8")
                
            else:
                print("\r")
                print("LIMITED GAME 8!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game8")
                limited += 1
        elif not "game9" in limited_game:
            time.sleep(3)
            data = game9()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 9")
                
            else:
                print("\r")
                print("LIMITED GAME 9!".format(ungu2, hijau2, ungu2, putih, hijau2))
                
                
                limited_game.append("game9")
                limited += 1
        elif not "game10" in limited_game:
            time.sleep(3)
            data = game10()
            if data['successFlag'] == True:
                num += 1
                print("\r")
                print(f"[{num}] SUCCESS CLAIM => GAME 10")
                
            else:
                print("\r")
                print("LIMITED GAME 10!".format(ungu2, hijau2, ungu2, putih, hijau2))
                limited_game.append("game10")
                app.config['status'] = "OFFLINE"
                app.config['limited_game'] = limited
                app.config['total_req'] = num
                
                print("LIMITED ALL!")

@app.route("/", methods=['GET','POST'])
def home():
    profile_data = profile()['data']
    return {
        "status":app.config['status'],
        "error_message": app.config['ERR_MESS'],
        "limited_game": app.config['limited_game'],
        "total_claim": app.config['total_req'],
        "country":profile_data['country'],
        "coin_balance":profile_data['balance'],
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "ram_usage": f"{psutil.virtual_memory().percent}%",
    }

@app.route('/start', methods=['GET','POST'])
def start_bot():
    if app.config['BOT_STARTED'] == False:
        if app.config['CAN_START'] == True:
            _thread.start_new_thread(mine, ())
            return "BOT STARTED!"
        else:
            return "TIDAK DAPAT MEMULAI BOT!"
    else:
        return "BOT ALREADY STARTED!"

def visit():
    while True:
        requests.get(config.visit_url)
        time.sleep(random.randint(1500, 1800))

account = profile()['data']
banner = f"""
{hijau2}
██████╗ ██╗      █████╗ ██╗   ██╗      ██████╗ ██╗      █████╗ ██╗   ██╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝      ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
██████╔╝██║     ███████║ ╚████╔╝ █████╗██████╔╝██║     ███████║ ╚████╔╝ 
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ╚════╝██╔═══╝ ██║     ██╔══██║  ╚██╔╝  
██║     ███████╗██║  ██║   ██║         ██║     ███████╗██║  ██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝         ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
                        ██████╗ ██████╗  █████╗                         
                        ██╔══██╗██╔══██╗██╔══██╗                        
                        ██████╔╝██████╔╝██║  ██║                        
                        ██╔═══╝ ██╔══██╗██║  ██║                        
                        ██║     ██║  ██║╚█████╔╝                        
{ungu2}================================>>||<<==================================
BY : JOJO
https://instagram.com/call_me.jojo

{red2}===============================>>NOTE<<=================================
SCRIPT INI GRATIS! HANYA MODAL MASUKKAN KODE REFFERAL!
TIDAK EXPIRED!
TIDAK DAPAT DI GUNAKAN JIKA PEMILIK APLIKASI SUDAH MEMPERBAIKI!

{yellow2}================================>>++<<==================================
==============================ACCOUNT INFO==============================
:-> USER ID = {account['userId']}
:-> COUNTRY = {account['country']}
:-> COIN BALANCE = {account['balance']}
================================>>++<<==================================
"""


if __name__ == '__main__': 
    print(banner)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=False)
    _thread.start_new_thread(visit, ())
