import os,requests,sys,time,json,httpx,random


def fingerprint():
    while True:
        proxylist =  open("data/proxies.txt", "r").read().splitlines()
        proxy = random.choice(proxylist)
        proxies = {
            "http://": f"http://{proxy}",
            "https://": f"http://{proxy}",
        }
        with httpx.Client(proxies=proxies) as client:
            try:
                x = client.get('https://discord.com/api/v9/experiments')
                return x.json()['fingerprint']
            except Exception as err:
                print(err)