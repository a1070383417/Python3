#!/usr/bin/python
#-*- coding:utf-8 -*-

import http.client,urllib,json,time,hashlib

#用户名
username =''

#密码
password =''

#token
#token1=''

#密钥
securitykey =''

#接单的金额
money ='100'

#选择运营商 1-移动，2-联通，3-电信，不填-任意 。填写多个使用英文逗号间隔:1,2
channel=''

#选择地区
prov=''

#接单单数默认不填为1
num =''
def main():
    #登陆
        conn = http.client.HTTPConnection(host='99shou.cn')
        conn.request(method ='POST',
                    url ='http://99shou.cn/api/user-server/user/login',
                    body =json.dumps({"username":username,"password":password}),
                    headers ={'Content-Type':'application/json;charset=utf-8'})
        #获取返回头,建立一个response对象
        response =conn.getresponse()
        #以response对象用read()函数接受返回头信息
        result=response.read().decode('utf-8')
        #json.loads是建立一个以json格式的对象.方便输出信息.
        data = json.loads(result)
        #print(data['rtnMsg'])
        #print('token=:%s' % data['rtnData']['token'])
        if data["rtnMsg"]=="获取token频繁，间隔至少1分钟以上!":
            print("获取token频繁，请等待10s!")
            time.sleep(10)
            main()
        #print(data["rtnMsg"])
        token1=data['rtnData']['token']
       
        conn.close()
        a=0
 ###获取13位的时间戳
        while 1:            
            t =time.time()
            txntime=int(round(t * 1000))
            txntime=str(txntime)
            ###
            #接单请求头的bodyjson
            bodyjson=json.dumps({"faceValue":money,"channel":channel,"prov":prov})
            ###md5认证
            md5=hashlib.md5()   
            data=bodyjson+securitykey+txntime
            md5.update(data.encode('utf-8'))
            sign=md5.hexdigest()
            ###
                #抢单
            #实例一个conn
            conn1= http.client.HTTPConnection(host='99shou.cn')
            #请求头
            conn1.request(method='POST',
                        url='http://99shou.cn/api/phonecharge-server/phonecharge/phone/receive',
                        headers={'Content-Type':'application/json;charset=utf-8','channelid':'OP0001','token':token1,'txntime':txntime,'sign':sign,},
                        body=bodyjson)
            #返回的信息+处理文本
            response1=conn1.getresponse()
            result1 = response1.read().decode('utf-8')
            data1= json.loads(result1)
            if response1.status == 200:                
                if data1['rtnCode']=='000000':
                    
                    print (data1['rtnMsg'])
                    print (data1['rtnData'])
                    exit()
            data1.setdefault("rtnMsg")
            data1.setdefault("rtnCode")
            a+=1
            print (a,data1['rtnMsg'])
            #print(data1["rtnCode"])
            if data1["rtnCode"]=="899993":
                main()
                break
            
            time.sleep(4)
            ###
if __name__ == '__main__':
        main()
