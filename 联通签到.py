#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
url="https://act.10010.com/SigninApp/signin/querySigninActivity.htm?version=android@6.002&desmobile=13058319130"
headers={
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; vivo NEX Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36; unicom{version:android@6.002,desmobile:13058319130};devicetype{deviceBrand:vivo,deviceModel:vivo NEX}",
     "Cookie": "upay_user=842b1b89ab02f7164dd01669c6d40b7b; WT_FPC=id=2875d594e3a9f99736c1552526401298:lv=1558042181531:ss=1558042181511; MUT_S=android7.1.1; clientid=98|0; JSESSIONID=y5pnchvZpKMzS8JnJ5x6TpX7w58hGFjrnS5Lcgfcxx7rSW7pYlWQ!1435514822; login_type=01; u_account=13058319130;"  

}
def main():
    response = requests.get(url,headers = headers)
    response.encoding="UTF-8"
    print(response.text)
if __name__ == '__main__':
        main()
