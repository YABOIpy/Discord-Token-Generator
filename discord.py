import modules, utils,requests,json,random,os,httpx,threading,names,datetime
from base64 import b64encode as encoder
from json import dumps
from utils import colors, messages
from fake_useragent import UserAgent

failed = 0
genned = 0
os.system('mode con: cols=75 lines=18')

def generate():
    global failed, genned
    while True:
    
        now = datetime.datetime.now().strftime("%H:%M:%S")
        proxylist = open("data/proxies.txt", "r").read().splitlines()
        proxy = random.choice(proxylist)
        proxies = {
            "http://": f"http://{proxy}",
            "https://": f"http://{proxy}",
        }
        finger = modules.fingerprint()
        agent = UserAgent().chrome
        year = random.randint(1970,2000)
        month = random.randint(00,12)
        day = random.randint(10,30)
        #password = names.get_full_name()
        #email = modules.getemail()
        payload = json.dumps({
            "fingerprint": finger,
            #"email": email,
            "username": names.get_full_name(),
            #"password": password,
            "invite": "dwncord",
            "consent": True,
            #"date_of_birth": f"{year}-{month}-{day}",
            #"gift_code_sku_id": None,
            "captcha_key": modules.bypass("4c672d35-0701-42b2-88c3-78380b0db560", "discord.com", 's'),
            #"promotional_email_opt_in": True
            })
        
        headers = {
            #'authority': 'discord.com',
            #'method': 'POST',
            'path': '/api/v9/auth/register',
            #'scheme': 'https',
            'accept-language': 'en-US,en;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'user-agent': "Discord/125.0 (iPad; iOS 15.4.1; Scale/2.00)",
            'content-type': 'application/json',
            'accept': '*/*',
            "referer": f"https://discord.com/invite/dwncord",
            #'origin': 'https://discord.com',
            #"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
            #'sec-fetch-site': 'same-origin',
            'sec-ch-ua-platform': 'iOS',
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            #'sec-ch-ua-mobile': '?0',
            #'sec-fetch-mode': 'cors',
            #'sec-fetch-dest': 'empty',
            #'referer': f"https://discord.com/register?email={email}",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            #"x-fingerprint": finger,
            #"x-super-properties": build_trackers(trackerType="x-super-properties")
        }
        with httpx.Client(proxies=proxies) as client:
            try:
                response = client.post("https://discord.com/api/v9/auth/register", headers=headers, data=payload)
                if response.status_code == 201:
                    token = response.json()['token']
                    ip = client.get('https://api.ipify.org/').text
                    halftoken = token[:len(token)//2]
                    genned =+1
                    print(f"{colors.blue}┃ {colors.white}({colors.blue}+{colors.white}) {halftoken}⋆ {colors.blue}|{colors.white} {now} {colors.blue}|{colors.white} {ip}")
                    x = open("data/tokens.txt", "a")
                    x.write(f'{token}' + "\n")  
                else:
                    print(f"Rate limit exceeded... {response.json()['retry_after']} ")
                    failed =+1
            except Exception as err:
                continue



def build_trackers(trackerType: str) -> str:
    """Builds the x-track/x-super-properties header"""
    if trackerType == "x-track":
        return encoder(dumps({"os":"iOS","browser":"Discord iOS","device":"iPad13,16","system_locale":"en-IN","client_version":"124.0","release_channel":"stable","device_advertiser_id":"00000000-0000-0000-0000-000000000000","device_vendor_id":"A1836CED-AD29-4FE0-B5C4-38444540AEA7","browser_user_agent":"","browser_version":"","os_version":"15.4.1","client_build_number": random.randint(0000,9999),"client_event_source":None}, separators=(',', ':')).encode()).decode()
    elif trackerType == "x-super-properties":
        return encoder(dumps({"os":"iOS","browser":"Discord iOS","device":"iPad13,16","system_locale":"en-IN","client_version":"124.0","release_channel":"stable","device_advertiser_id":"00000000-0000-0000-0000-000000000000","device_vendor_id":"A1836CED-AD29-4FE0-B5C4-38444540AEA7","browser_user_agent":"","browser_version":"","os_version":"15.4.1","client_build_number": random.randint(0000,9999),"client_event_source":None}, separators=(',', ':')).encode()).decode()
    else:
        raise Exception(
            "Invalid tracker type. Currently support types('x-track', 'x-super-properties')")

def _submit_trackers():
    return client.post("https://discord.com/api/v9/track/ott", json={"type": "landing"})

