# 登录-单接口测试用例
from api.login import LoginApi
import pytest
import json
import config

def getfile(json_file):

    test_data = []
    # 以只读形式打开文件
    with open(json_file,'r',encoding='utf-8') as fp:
        # 加载文件中的json数据
        json_data = json.load(fp)
        for case_data in json_data:
            username = case_data["username"]
            password = case_data["password"]
            status = case_data["status"]
            message = case_data["message"]
            code = case_data["code"]
            test_data.append((username,password,status,message,code))
            # [(),()]

            return test_data



class TestLoginCase:

    uuid = None

    def setup(self):

        self.login_api = LoginApi()
        vetify_res = self.login_api.vetify_code()
        TestLoginCase.uuid = vetify_res.json()["uuid"]

    def teardown(self):
        pass

    # 1.登录  [[(),()..],[(),()..]]
    @pytest.mark.parametrize("username,password,status,message,code",getfile(json_file=config.BASE_PATH + '/data/login.json'))
    def test01_login_case(self,username,password,status,message,code):

        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginCase.uuid
        }
        res = self.login_api.login(login_data)

        assert status == res.status_code
        assert message in res.text
        assert code == res.json().get("code")
