#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
def a():
    r = requests.post(url="https://m.client.10010.com/mobileService/login.htm",
                data={
                    "isRemberPwd":"true","password":"kdBepYGxTO1QYsM1qCpWzWLJr61IJg0IZTbsZU+ZaBSaRRm3N599UqTX/n0D3DehsonzG5O0plwQhIpzOcm3AMM6Fbujhi2zWG2JyyyNaZkz08D6dTGatqO3+dnY/W9Uig+kbpxPcpOhoVqPpq7dJOHQffPEamCXToN1+V4EEc0=","deviceId":"866700036044061","netWay":"WIFI","mobile":"IfONaSVHRWnyZcP6f9L1JIB47quFOnfvfAF0fvU7dlJ98ESfvs9Ebw3vHy0fVQKK3D8VrYr9dl81j7BVfXahvE6Y5lHdgwu2+jVgp0PVay8hQVrHE/0lBpNEvkxfNVhn8AURSn/1DyUzs64sfkhelsZrQdqy9MsIhKq6d/zIc1U=","timestamp":"20190522205808","appId":"1f7af72ad6912d306b5053abf90c7ebba1d48305581ce1ac2191a208b1f3ee88ed4fdb7142841b815e7c26b05d7b4970611d2a2c65f0088d626223eb69c9c36e","keyVersion":"1","deviceBrand":"vivo","areaCode":"530","provinceChanel":"general","version":"android@6"
                },verify=False)
    d="ecs_token="+r.cookies['third_token']

    
    headers={
    "Cookie":d,
    'Content-Type':"text/html;charset=UTF-8"
        }
  
  
    r1 = requests.post(url="https://act.10010.com/SigninApp/signin/querySigninActivity.htm?version=android@6.002&desmobile=13058319130",headers=headers,verify=False)
    
    JSESSIONID="JSESSIONID="+r1.cookies["JSESSIONID"]
    route5="route5="+r1.cookies["route5"]

    headers1={
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; vivo NEX Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36; unicom{version:android@6.002,desmobile:13058319130};devicetype{deviceBrand:vivo,deviceModel:vivo NEX}",
    'Content-Type':'application/json;charset=utf-8',
     "Cookie":route5+";"+JSESSIONID
    }
    #print(d)
    #################################################################################
    r2 = requests.post(url="https://act.10010.com/SigninApp/signin/daySign.do",headers=headers1,verify=False)
    if "0001" in r2.text:
        print("r2.text")
if __name__ == '__main__':
        a()
