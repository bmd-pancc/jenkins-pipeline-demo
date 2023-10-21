from api.login import LoginApi
from api.course import CourseAPI

# 单接口测试-添加课程模块
class TestCourseCase:

    token = None

    def setup(self):

        self.login_api = LoginApi()
        self.course_api = CourseAPI()
        # 获取验证码
        vetify_res = self.login_api.vetify_code()
        uuid = vetify_res.json().get("uuid")
        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        res_login = self.login_api.login(login_data)
        TestCourseCase.token = res_login.json().get("token")


    def teardown(self):
        pass

    # 1.添加课程成功(全部参数填写正确)
    def test01_add_course_success(self):

        add_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课02"
        }

        res = self.course_api.add_course(add_data,TestCourseCase.token)
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")


    # 2.添加课程失败(未登录)
    def test02_course_name_null(self):
        add_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课02"
        }
        res = self.course_api.add_course(add_data,"xxx")
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 401 == res.json().get("code")
