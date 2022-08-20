import random,base64
from fake_useragent import UserAgent


def xprop()
    null = "null"
    browsers = "google", "operaGX"
    drivers = "chrome", "edge", "firefox", "brave"
    driver = random.choice(drivers)
    browser = random.choice(browsers)
    agent = UserAgent().chrome
    content = {
        "os":"windows",
        "browser":"Chrome",
        "device":"",
        "system_locale":"en-US",
        "browser_user_agent": f"{agent}",
        "browser_version":"103.0.0.0",
        "os_version":"10",
        "referrer":f"https://www.{browser}.com/",
        "referring_domain":f"www.{browser}.com",
        "search_engine":"google",
        "referrer_current":f"https://www.{browser}.com/",
        "referring_domain_current":f"www.{browser}.com",
        "search_engine_current":f"{browser}",
        "release_channel":"stable",
        "client_build_number":random.randint(1300000,140000),
        "client_event_source":null
    }

    xsprprop = base64.b64decode(content.encode('utf-8')).decode('utf-8')
    print(xsprprop)


    import json,random
    from fake_useragent import UserAgent
    from base64 import b64encode as b

    agent = UserAgent().chrome
    super_properties = b(json.dumps({
                "os": "Windows",
                "browser": "Firefox",
                "device": "",
                "system_locale": "en-US",
                "browser_user_agent": agent,
                "browser_version": "90.0",
                "os_version": "10",
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "",
                "referring_domain_current": "",
                "release_channel": "stable",
                "client_build_number": random.randint(1300000,140000),
                "client_event_source": None
            }, separators=(',', ':')).encode()).decode()