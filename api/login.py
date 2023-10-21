import requests
# 接口对象层
# 登录模块
import config

class LoginApi:


    def __init__(self):
        self.vetify_code_url = config.BASE_URL + '/api/captchaImage'
        self.login_url = config.BASE_URL + '/api/login'

    # 获取验证码
    def vetify_code(self):
        res = requests.get(url=self.vetify_code_url)
        return res


    # 登录
    def login(self,data):
        res = requests.post(url=self.login_url,json=data)
        return res
