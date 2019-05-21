#!/usr/bin/python
#-*- coding:utf-8 -*-

import http.client,urllib,json,time,hashlib
body=json.dumps({
"clientId":"357","userId":"tYYokVXsjritBSVd1MmPPT4qRG9CYWgMVA7GSTO9pUP9551BbK15N281U0JnLI7FDlsg67REKtu3\n9wJWPLyXJdpUvUBt3CQ9oGKufTZMkencyHDmVlK552vW9d,tSN7oHqRtGuP9PrvqxHmu4a3venr7\nG,ylWXf5/MOd4jbyAwKzZ0/F,5HnDwPeMiGb3PQGGUc4w8eCce7Fd9UPVAvXRe1JEVVRWcbJkgoY\nuf4TtC2X2lK/,Siv4IbeRJO2Kkw5xcvasT5MDngVDGWLnBWgT3yPNG5na/p56jUf1ZPQqqFdamIx\ncAAVZnR48ev8eiW7eiPCLEam2Sb5/yld2Q9,6403QjjsgGFXQ,K17TPvWtSYviNNkZPuSAYumYaY\n/mg7SJ/zLk3h5Z,bo73Mtk2bI7FG8C,vcACvGeepI6cGsh248F1JymHzM2ny/Xe5yKk63wSJGuJo\nQn1Q7eqocRrSMA==","authType":"JHWY_SIGNIN","actionParams":{"actionNo":"ACT_MZESQFXG","actionCode":""},"t":0.8602675508137678
})
def main():
    conn = http.client.HTTPConnection(host='promotion.phone580.com')
    conn.request(method ='POST',
                    url ='https://promotion.phone580.com/fmapi/api/action/collect-user-action',
                    body =body,
                    headers ={'Content-Type':'application/json;charset=utf-8'})
    #返回的信息+处理文本
    response=conn.getresponse()
    result1 = response.read().decode('utf-8')
    print(result1)
if __name__ == '__main__':
    for i in range(1,10):
        main()