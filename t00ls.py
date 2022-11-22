import requests
import json

#Tools用户名
username="XX"

#password的md5，要用全小写
password="1245aaaaaaaaaaaaaaaaaaaa"

#tools账号问题
# 1 =母亲的名字
# 2 =爷爷的名字
# 3 =父亲出生的城市
# 4 =您其中一位老师的名字
# 5 =您个人计算机的型号
# 6 =您最喜欢的餐馆名称
# 7 =驾驶执照的最后四位数字
questionid="4"

#明文的问题答案
answer="t00ls"

#t00ls的其他域名，用于单一域名故障时
t00lsdomain=["www.t00ls.com","www.t00ls.cc","www.t00ls.net"]

#方糖server酱推送url，类似如下
fangtangpushurl="https://sctapi.ftqq.com/Sxxxxxxxxxxxxxxxo.send?title="

##bark推送url，类似如下
barkpushurl="http://8.8.8.8:8888/6xxxxxxxxxxxxxxxW/"

class sendmessage():
    def __init__(self,title="",message=""):
        self.title=title
        self.message=message
    def fangtang(self):
        requests.get(fangtangpushurl+self.title+"&desp="+self.message)
    def bark(self):
        requests.get(barkpushurl+self.title+"/"+self.message+"/")


class t00lsuser():
    def __init__(self):
        self.login_data = {
            'action': 'login',
            'username': username,
            'password': password,
            'questionid': questionid,
            'answer': answer
        }

        self.formhash=""
        self.t00ls_cookies=""

    def login(self,domain):
        for domain in t00lsdomain:
            response_login = requests.post('https://'+domain+'/login.json', data=self.login_data)
            response_login_json = json.loads(response_login.text)
            if response_login_json['status'] != 'success':
                continue
            else:
                print('用户:', username, '登入成功!')
                break
        self.formhash = response_login_json['formhash']
        self.t00ls_cookies = response_login.cookies

    def sign(self):

        sign_data = {
            'formhash': self.formhash,
            'signsubmit': "true"
        }
        response_sign = requests.post('https://www.t00ls.com/ajax-sign.json', data=sign_data, cookies=self.t00ls_cookies)

        try:
            if(json.loads(response_sign.text)['status'] == 'success'):
                return('签到成功 TuBi + 1')
            elif(json.loads(response_sign.text)['message'] == 'alreadysign'):
                return('已经签到过啦')
            else:
                return("签到失败")
        except:
            return("出现错误，签到失败")


if __name__ == '__main__':
    t00lsuser=t00lsuser()
    #登录
    t00lsuser.login(t00lsdomain)
    #签到
    signret=t00lsuser.sign()
    print(signret)

    #发消息
    sendmessage=sendmessage("t00ls签到脚本",signret)
    sendmessage.bark()

    

    
