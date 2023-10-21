# 登录-单接口测试用例
from api.login import LoginApi
from utils.read_data import get_data
import pytest




class TestLoginCase:

    uuid = None

    def setup(self):

        self.login_api = LoginApi()
        vetify_res = self.login_api.vetify_code()
        TestLoginCase.uuid = vetify_res.json()["uuid"]

    def teardown(self):
        pass

    # 1.登录
    @pytest.mark.parametrize("username,password,status,message,code",get_data()["login_data"])
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

"""
数据驱动: parametrize+yaml的练习
"""