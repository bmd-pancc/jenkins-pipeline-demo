# 脚本层
from api.login import LoginApi
from api.course import CourseAPI
from api.contract import ContractAPI
import config

class TestContractBusinessAPI:

    token = None
    fileName = None

    def setup(self):

        self.login_api = LoginApi()
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

    def teardown(self):
        pass

    # 登录成功
    def test01_login(self):

        # 获取验证码
        res_vetify = self.login_api.vetify_code()
        uuid = res_vetify.json().get('uuid')
        # 登录
        login_data = {
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":uuid
        }
        res_login = self.login_api.login(login_data)
        TestContractBusinessAPI.token = res_login.json().get('token')

    # 添加课程成功
    def test02_add_course(self):

        add_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }

        res = self.course_api.add_course(data=add_data,token=TestContractBusinessAPI.token)


    # 课程查询成功
    def test03_select_course(self):

        res = self.course_api.select_course(test_data="",token=TestContractBusinessAPI.token)

    # 课程修改成功
    # 课程删除成功

    # 合同上传成功
    def test04_contract_upload(self):

        fp = open(config.BASE_PATH + '/data/test.txt','rb')
        res = self.contract_api.contract_upload(data=fp,token=TestContractBusinessAPI.token)
        TestContractBusinessAPI.fileName = res.json()["fileName"]

    # 新增合同成功
    def test05_add_contract(self):

        add_data = {
            "name": "测试888",
            "phone": "13145115211",
            "contractNo": "HT2077100608091",
            "subject": "6",
            "courseId": 99,
            "channel": "0",
            "activityId": 77,
            "fileName": TestContractBusinessAPI.fileName
        }

        res = self.contract_api.contract_add(data=add_data,token=TestContractBusinessAPI.token)

    # 合同查询成功
    def test06_select_contract(self):

        res = self.contract_api.contract_select(TestContractBusinessAPI.token)
